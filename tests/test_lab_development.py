"""The development bench executes the player's sequence against real lab rules."""
import copy
import pathlib
import textwrap
import unittest

from test_lab_state import load_state


SOURCE = pathlib.Path(__file__).resolve().parents[1] / "scripts/lab_development.rpy"


class LabDevelopmentTests(unittest.TestCase):
    def setUp(self):
        self.assertTrue(SOURCE.exists(), "The playable development bench must exist")
        self.state, self.api = load_state()
        source = SOURCE.read_text(encoding="utf-8")
        for line in source.splitlines():
            if line.startswith("default "):
                name, value = line[8:].split(" = ", 1)
                setattr(self.state, name, eval(value))
        code = source.split("init python:\n", 1)[1].split("\nlabel ", 1)[0]
        exec(compile(textwrap.dedent(code), str(SOURCE), "exec"), self.api)
        self.state.lab_plan = ["conflict", "preparation"]
        self.api["lab_dev_reset"]()

    def call(self, name, *args):
        return self.api[name](*args)

    def test_early_write_leaves_rejected_candidate_in_copy(self):
        for case, result in [("invalid", "invalid"), ("overlap", "conflict")]:
            with self.subTest(case=case):
                report = self.call("lab_dev_execute", ["save", "validate", "rules"], case, self.state.lab_plan)
                self.assertEqual(report["result"], result)
                self.assertTrue(report["dirty"])
                self.assertEqual(len(report["reservations"]), 2)
                self.assertEqual(report["reservations"][0], ("microscopio", 840, 900))

    def test_validation_before_write_preserves_existing_reservation(self):
        for case, result in [("invalid", "invalid"), ("overlap", "conflict"), ("preparation", "preparation_required")]:
            with self.subTest(case=case):
                report = self.call("lab_dev_execute", ["validate", "rules", "save"], case, self.state.lab_plan)
                self.assertEqual(report["result"], result)
                self.assertFalse(report["dirty"])
                self.assertEqual(report["reservations"], [("microscopio", 840, 900)])

    def test_validation_alone_does_not_protect_conflict_when_write_is_in_middle(self):
        report = self.call("lab_dev_execute", ["validate", "save", "rules"], "overlap", self.state.lab_plan)
        self.assertEqual(report["result"], "conflict")
        self.assertTrue(report["dirty"])
        self.assertEqual(report["reservations"], [("microscopio", 840, 900), ("microscopio", 870, 930)])

    def test_tests_do_not_implement_missing_rules_or_mutate_fixtures(self):
        before = copy.deepcopy(self.api["LAB_CASES"])
        self.state.lab_plan = ["clarity"]
        self.state.lab_dev_order = ["validate", "rules", "save"]
        for case in ["invalid", "overlap", "preparation", "other"]:
            self.call("lab_dev_run", case)
        self.assertEqual(self.state.lab_dev_results["overlap"]["result"], "allowed")
        self.assertEqual(self.state.lab_dev_results["preparation"]["result"], "allowed")
        self.assertEqual(self.state.lab_plan, ["clarity"])
        self.assertEqual(self.api["LAB_CASES"], before)
        self.assertEqual(self.state.lab_test_results, {})
        self.assertTrue(self.call("lab_dev_ready"))

    def test_order_edit_swaps_steps_and_invalidates_old_test_evidence(self):
        self.call("lab_dev_run", "invalid")
        self.call("lab_dev_select", "validate")
        self.assertTrue(self.call("lab_dev_place", 0))
        self.assertEqual(self.state.lab_dev_order, ["validate", "save", "rules"])
        self.assertEqual(self.state.lab_dev_results, {})
        self.assertFalse(self.call("lab_dev_ready"))
        before = copy.deepcopy(vars(self.state))
        self.assertFalse(self.call("lab_dev_place", -1))
        self.assertFalse(self.call("lab_dev_select", "invented"))
        self.assertEqual(self.state.lab_dev_order, before["lab_dev_order"])

    def test_release_requires_fresh_regression_for_every_scenario(self):
        for case in ["invalid", "overlap", "preparation", "other"]:
            self.call("lab_dev_run", case)
        self.assertFalse(self.call("lab_dev_ready"))
        self.state.lab_dev_order = ["validate", "rules", "save"]
        self.state.lab_dev_results = {}
        for case in ["invalid", "overlap", "preparation"]:
            self.call("lab_dev_run", case)
        self.assertFalse(self.call("lab_dev_ready"))
        self.call("lab_dev_run", "other")
        self.assertTrue(self.call("lab_dev_ready"))
        self.assertEqual(self.state.lab_dev_results["other"]["reservations"], [("microscopio", 840, 900), ("centrifuga", 840, 900)])

    def test_pair_review_runs_concrete_boundary_case_and_reset_clears_revision(self):
        self.state.lab_plan = ["conflict"]
        self.call("lab_dev_review", "pair")
        self.assertEqual(self.state.lab_dev_mode, "pair")
        self.assertIn("adjacent", self.state.lab_dev_results)
        self.assertEqual(self.state.lab_dev_results["adjacent"]["result"], "allowed")
        self.assertNotIn("preparation", self.state.lab_plan)
        self.state.lab_revision = 2
        self.call("lab_dev_reset")
        self.assertEqual(self.state.lab_dev_revision, 2)
        self.assertEqual(self.state.lab_dev_results, {})
        self.assertEqual(self.state.lab_dev_mode, "")
        self.assertEqual(self.state.lab_dev_order, ["save", "validate", "rules"])


if __name__ == "__main__":
    unittest.main()
