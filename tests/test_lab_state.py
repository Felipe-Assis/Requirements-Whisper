"""Fast domain checks; Ren'Py tests cover engine persistence separately."""
import copy
import pathlib
import textwrap
import types
import unittest


SOURCE = pathlib.Path(__file__).resolve().parents[1] / "scripts/project_state.rpy"


def load_state():
    source = SOURCE.read_text(encoding="utf-8")
    namespace = {}
    store = types.SimpleNamespace()
    for line in source.splitlines():
        if line.startswith("default "):
            name, value = line[8:].split(" = ", 1)
            setattr(store, name, eval(value))
    namespace["store"] = store
    exec(compile(textwrap.dedent(source.split("init python:\n", 1)[1]), str(SOURCE), "exec"), namespace)
    return store, namespace


class LabStateTests(unittest.TestCase):
    def setUp(self):
        self.assertTrue(SOURCE.exists(), "Campaign state and rules must exist")
        self.state, self.api = load_state()
        self.call("lab_reset")

    def call(self, name, *args):
        return self.api[name](*args)

    def select(self, *items):
        for item in items:
            self.assertTrue(self.call("lab_toggle_plan", item))

    def test_calendar_half_open_intervals_and_equipment(self):
        existing = ("microscope", 840, 900)
        self.assertEqual(self.call("lab_reservation_result", existing, ("microscope", 870, 930), ["conflict"]), "conflict")
        self.assertEqual(self.call("lab_reservation_result", existing, ("microscope", 900, 930), ["conflict"]), "allowed")
        self.assertEqual(self.call("lab_reservation_result", existing, ("centrifuge", 870, 930), ["conflict", "preparation"]), "allowed")
        self.assertEqual(self.call("lab_reservation_result", existing, ("microscope", 870, 930), []), "allowed")

    def test_preparation_ten_minutes_applies_only_to_microscope(self):
        for candidate in [("microscope", 900, 930), ("microscope", 810, 835)]:
            self.assertEqual(self.call("lab_reservation_result", ("microscope", 840, 900), candidate, ["conflict", "preparation"]), "preparation_required")
        self.assertEqual(self.call("lab_reservation_result", ("microscope", 840, 900), ("microscope", 910, 930), ["conflict", "preparation"]), "allowed")
        self.assertEqual(self.call("lab_reservation_result", ("centrifuge", 840, 900), ("centrifuge", 900, 930), ["conflict", "preparation"]), "allowed")

    def test_invalid_calendar_entries_never_become_reservations(self):
        for candidate in [("microscope", 900, 840), ("microscope", 900, 900), ("microscope", -1, 30), ("microscope", True, 900), ("microscope", 900, 1500), ("", 900, 930), ("microscope", "900", 930), None]:
            self.assertEqual(self.call("lab_reservation_result", ("microscope", 840, 900), candidate, []), "invalid")

    def test_evidence_has_source_and_hypotheses_can_be_revised(self):
        self.assertFalse(self.call("lab_link", "conflict", "sheets"))
        self.call("lab_collect", "sheets")
        self.call("lab_collect", "sheets")
        self.assertEqual(self.state.lab_evidence, ["sheets"])
        self.assertFalse(self.call("lab_link", "preparation", "sheets"))
        self.assertEqual(self.state.lab_links["preparation"], "sheets")
        self.call("lab_collect", "preparation")
        self.assertTrue(self.call("lab_link", "preparation", "preparation"))
        self.call("lab_collect", "offline")
        self.assertTrue(self.state.lab_sidequest)
        before = copy.deepcopy(vars(self.state))
        self.assertFalse(self.call("lab_collect", "made_up"))
        self.assertEqual(self.state.lab_evidence, before["lab_evidence"])

    def test_capacity_and_dependencies_are_atomic(self):
        self.assertFalse(self.call("lab_plan_ready"))
        self.assertFalse(self.call("lab_toggle_plan", "preparation"))
        self.select("conflict", "preparation")
        self.assertEqual(self.call("lab_plan_cost"), 3)
        self.assertFalse(self.call("lab_toggle_plan", "clarity"))
        self.assertEqual(self.state.lab_plan, ["conflict", "preparation"])
        self.assertFalse(self.call("lab_toggle_plan", "conflict"))
        self.assertTrue(self.call("lab_plan_ready"))
        self.assertTrue(self.call("lab_toggle_plan", "preparation"))
        self.assertTrue(self.call("lab_toggle_plan", "conflict"))
        self.assertEqual(self.state.lab_plan, [])

    def test_commitment_does_not_invent_protection(self):
        self.assertFalse(self.call("lab_confirm_commitment", "base_primeiro"))
        self.select("clarity")
        self.assertTrue(self.call("lab_confirm_commitment", "base_primeiro"))
        self.assertEqual(self.state.lab_delivery, "not_delivered")
        self.assertNotIn("base_delivered", self.state.lab_events)
        self.assertTrue(self.call("lab_mark_delivery"))
        self.assertEqual(self.state.lab_delivery, "base_delivered")
        self.assertEqual(self.call("lab_run_test", "overlap"), "allowed")
        self.assertEqual(self.call("lab_ending"), "unowned")
        self.call("lab_mark_delivery")
        self.assertEqual(self.state.lab_events.count("base_delivered"), 1)

    def test_investigation_is_pending_even_with_good_plan(self):
        self.select("conflict", "preparation")
        self.call("lab_confirm_commitment", "investigar_agora")
        self.assertEqual(self.state.lab_delivery, "not_delivered")
        self.assertEqual(self.state.lab_commitment_status, "open")
        self.assertTrue(self.state.lab_commitment_owner)
        self.assertTrue(self.state.lab_return_milestone)
        self.assertEqual(self.call("lab_ending"), "waiting")
        self.assertNotIn("dependency_found", self.state.lab_events)
        self.assertEqual(self.call("lab_run_test", "overlap"), "conflict")
        self.assertFalse(self.call("lab_mark_delivery"))
        self.assertEqual(self.call("lab_ending"), "waiting")

    def test_no_test_is_not_a_product_bug_and_repair_preserves_history(self):
        self.select("conflict", "preparation")
        self.call("lab_confirm_commitment", "base_primeiro")
        self.call("lab_mark_delivery")
        self.assertEqual(self.state.lab_test_results, {})
        self.assertEqual(self.call("lab_ending"), "reliable")
        self.call("lab_collect", "sheets")
        self.call("lab_repair")
        self.call("lab_repair")
        self.assertEqual(self.state.lab_revision, 2)
        self.assertEqual(self.state.lab_commitment, "base_primeiro")
        self.assertEqual(self.state.lab_evidence, ["sheets"])
        self.assertNotIn("repaired", self.state.lab_events)
        self.assertEqual(self.call("lab_ending"), "unowned")
        self.assertEqual(self.call("lab_run_test", "preparation"), "preparation_required")
        self.assertEqual(self.call("lab_run_test", "overlap"), "conflict")
        self.assertTrue(self.call("lab_mark_delivery"))
        self.assertTrue(self.call("lab_mark_delivery"))
        self.assertEqual(self.state.lab_events.count("repaired"), 1)
        self.assertEqual(self.call("lab_ending"), "repaired")

    def test_invalid_actions_do_not_overwrite_real_decisions(self):
        self.select("conflict")
        self.call("lab_confirm_commitment", "base_primeiro")
        before = copy.deepcopy(vars(self.state))
        self.assertFalse(self.call("lab_confirm_commitment", "unknown"))
        self.assertFalse(self.call("lab_toggle_plan", "unknown"))
        self.assertEqual(self.call("lab_run_test", "unknown"), "invalid")
        for name in ["lab_plan", "lab_events", "lab_commitment", "lab_delivery", "lab_test_results"]:
            self.assertEqual(getattr(self.state, name), before[name])

    def test_repair_requires_fresh_regression_results(self):
        self.select("clarity")
        self.call("lab_confirm_commitment", "base_primeiro")
        self.call("lab_mark_delivery")
        self.call("lab_run_test", "overlap")
        self.assertEqual(self.state.lab_test_results["overlap"], "allowed")
        self.call("lab_repair")
        self.assertEqual(self.state.lab_test_results, {})
        self.assertEqual(self.state.lab_delivery, "revision_pending")
        self.assertFalse(self.call("lab_mark_delivery"))
        self.assertNotIn("repaired", self.state.lab_events)
        self.assertEqual(self.call("lab_ending"), "unowned")
        self.assertEqual(self.call("lab_run_test", "overlap"), "conflict")
        self.assertFalse(self.call("lab_mark_delivery"))
        self.assertEqual(self.call("lab_run_test", "preparation"), "preparation_required")
        self.assertEqual(self.state.lab_delivery, "revision_pending")
        self.assertTrue(self.call("lab_mark_delivery"))
        self.assertEqual(self.state.lab_delivery, "repaired")
        self.assertEqual(self.call("lab_ending"), "repaired")

    def test_repair_preserves_original_scope_and_adds_a_separate_round(self):
        self.select("clarity")
        self.call("lab_confirm_commitment", "base_primeiro")
        self.call("lab_mark_delivery")
        self.call("lab_repair")
        self.assertIn("clarity", self.state.lab_plan)
        self.assertEqual(self.state.lab_initial_plan, ["clarity"])
        self.assertEqual(set(self.state.lab_plan), {"clarity", "conflict", "preparation"})
        self.assertEqual(self.call("lab_plan_cost"), 4)
        self.call("lab_repair")
        self.assertEqual(self.state.lab_initial_plan, ["clarity"])
        self.assertEqual(len(self.state.lab_plan), 3)

    def test_integration_is_a_dedicated_investigation_not_a_plan_item(self):
        self.assertNotIn("integration", self.api["LAB_ITEMS"])
        self.assertFalse(self.call("lab_toggle_plan", "integration"))
        self.assertEqual(self.state.lab_plan, [])

    def test_delivery_requires_an_explicit_base_commitment(self):
        self.assertFalse(self.call("lab_mark_delivery"))
        self.assertEqual(self.state.lab_delivery, "not_delivered")

    def test_reset_clears_campaign_without_changing_preferences(self):
        self.state.player_name = "Pat"
        self.select("clarity")
        self.call("lab_collect", "offline")
        self.call("lab_confirm_commitment", "investigar_agora")
        self.call("lab_run_test", "overlap")
        self.call("lab_repair")
        self.call("lab_reset")
        self.assertTrue(self.state.lab_active)
        self.assertEqual(self.state.lab_phase, "investigation")
        self.assertEqual(self.state.lab_evidence, [])
        self.assertEqual(self.state.lab_plan, [])
        self.assertEqual(self.state.lab_initial_plan, [])
        self.assertEqual(self.state.lab_test_results, {})
        self.assertFalse(self.state.lab_repaired)
        self.assertFalse(self.state.lab_sidequest)
        self.assertEqual(self.state.lab_revision, 1)
        self.assertEqual(self.state.lab_commitment, "")
        self.assertEqual(self.state.player_name, "Pat")

    def test_objective_is_defined_for_each_phase(self):
        for phase in ["investigation", "definition", "planning", "negotiation", "delivery", "followup", "ending"]:
            self.state.lab_phase = phase
            self.assertTrue(self.call("lab_objective"))


if __name__ == "__main__":
    unittest.main()
