"""Rules exercised independently of Ren'Py; engine journeys cover the UI."""
import copy
import pathlib
import textwrap
import types
import unittest

SOURCE = pathlib.Path(__file__).resolve().parents[1] / "scripts/tickets_state.rpy"


def load_state():
    namespace = {"store": types.SimpleNamespace()}
    source = SOURCE.read_text(encoding="utf-8")
    for line in source.splitlines():
        if line.startswith("default "):
            name, value = line[8:].split(" = ", 1)
            setattr(namespace["store"], name, eval(value))
    exec(compile(textwrap.dedent(source.split("init python:\n", 1)[1]), str(SOURCE), "exec"), namespace)
    return namespace["store"], namespace


class TicketStateTests(unittest.TestCase):
    def setUp(self):
        self.assertTrue(SOURCE.exists(), "Ticket campaign rules must exist")
        self.state, self.api = load_state()
        self.call("ticket_reset")

    def call(self, name, *args):
        return self.api[name](*args)

    def prepared(self, policy="publish_followup", owner="sabrina"):
        for source in ("panel", "message", "log"):
            self.call("ticket_collect", source)
        self.call("ticket_prioritize", "241")
        self.call("ticket_demo", "old", "resolved")
        self.call("ticket_choose_patch", "atomic")
        for case in ("resolved", "empty", "other"):
            self.call("ticket_demo", "new", case)
        self.call("ticket_set_policy", policy)
        self.call("ticket_choose_solution", "public")
        self.call("ticket_handoff", owner)

    def test_reset_isolates_campaigns_and_copies_initial_records(self):
        self.state.lab_plan = ["keep"]
        self.state.campaign_results = {"lab": {"summary": "keep"}}
        self.call("ticket_prioritize", "241")
        self.state.ticket_records["241"]["history"].append("edited")
        self.call("ticket_reset")
        self.assertEqual(self.state.lab_plan, ["keep"])
        self.assertEqual(self.state.campaign_results, {"lab": {"summary": "keep"}})
        self.assertNotIn("edited", self.state.ticket_records["241"]["history"])

    def test_sources_and_priority_are_explicit_without_scores(self):
        self.assertFalse(self.call("ticket_collect", "made_up"))
        for source in ("panel", "message", "log", "shift"):
            self.assertTrue(self.call("ticket_collect", source))
        self.call("ticket_collect", "shift")
        self.assertEqual(len(self.state.ticket_evidence), 4)
        for ticket_id in ("241", "242", "243"):
            self.assertTrue(self.call("ticket_prioritize", ticket_id))
            self.assertTrue(self.call("ticket_priority_impact"))
        self.assertFalse(self.call("ticket_prioritize", "made_up"))
        self.assertEqual(self.state.ticket_selected, "243")

    def test_old_version_reproduces_divergence_and_new_publishes_both(self):
        self.call("ticket_prioritize", "241")
        self.assertEqual(self.call("ticket_demo", "old", "resolved"), "divergent")
        self.assertEqual(self.state.ticket_demo_records["241"]["internal_status"], "Resolvido")
        self.assertEqual(self.state.ticket_demo_records["241"]["public_status"], "Em atendimento")
        self.call("ticket_choose_patch", "atomic")
        self.assertEqual(self.call("ticket_demo", "new", "resolved"), "published")
        self.assertEqual(self.state.ticket_demo_records["241"]["public_status"], "Resolvido")
        self.assertIn("matrícula", self.state.ticket_demo_records["241"]["public_solution"])
        self.assertEqual(self.state.ticket_records["241"]["public_status"], "Em atendimento")

    def test_empty_solution_is_rejected_atomically(self):
        self.call("ticket_choose_patch", "atomic")
        self.assertEqual(self.call("ticket_demo", "new", "empty"), "blocked")
        self.assertEqual(self.state.ticket_demo_records, self.state.ticket_records)
        self.assertEqual(self.call("ticket_demo", "old", "empty"), "empty_resolved")

    def test_resolution_does_not_change_other_tickets(self):
        self.call("ticket_prioritize", "242")
        self.call("ticket_choose_patch", "atomic")
        before = copy.deepcopy(self.state.ticket_records)
        self.assertEqual(self.call("ticket_demo", "new", "other"), "isolated")
        self.assertEqual(self.state.ticket_demo_records["241"], before["241"])
        self.assertEqual(self.state.ticket_demo_records["243"], before["243"])
        self.assertEqual(self.state.ticket_demo_records["242"]["public_status"], "Resolvido")

    def test_wrong_patch_cannot_be_released_and_revisions_clear_tests(self):
        self.prepared()
        self.assertTrue(self.call("ticket_tests_ready"))
        self.call("ticket_choose_patch", "internal")
        self.assertEqual(self.state.ticket_tests, {})
        self.assertEqual(self.call("ticket_demo", "new", "resolved"), "divergent")
        self.assertFalse(self.call("ticket_submit"))
        self.call("ticket_choose_patch", "broadcast")
        self.assertEqual(self.call("ticket_demo", "new", "other"), "leaked")
        self.assertFalse(self.call("ticket_tests_ready"))

    def test_publication_requires_reproduction_and_all_regressions(self):
        self.call("ticket_choose_patch", "atomic")
        for case in ("resolved", "empty", "other"):
            self.call("ticket_demo", "new", case)
        self.call("ticket_set_policy", "publish_followup")
        self.call("ticket_choose_solution", "public")
        self.call("ticket_handoff", "sabrina")
        self.assertFalse(self.call("ticket_submit"))
        self.call("ticket_demo", "old", "resolved")
        for source in ("panel", "message", "log"):
            self.call("ticket_collect", source)
        self.assertTrue(self.call("ticket_submit"))

    def test_internal_note_or_empty_draft_never_becomes_public(self):
        self.prepared()
        for draft in ("internal", "empty"):
            self.call("ticket_choose_solution", draft)
            before = copy.deepcopy(self.state.ticket_records)
            self.assertFalse(self.call("ticket_submit"))
            self.assertEqual(self.state.ticket_records, before)
        self.call("ticket_choose_solution", "public")
        self.assertTrue(self.call("ticket_submit"))
        record = self.state.ticket_records["241"]
        self.assertNotEqual(record["public_solution"], record["internal_note"])

    def test_review_policy_waits_for_colleague_before_publication(self):
        self.prepared("peer_review")
        self.assertTrue(self.call("ticket_submit"))
        self.assertEqual(self.state.ticket_delivery, "review_pending")
        self.assertEqual(self.state.ticket_records["241"]["public_status"], "Em atendimento")
        self.assertEqual(self.state.ticket_records["241"]["public_solution"], "")
        self.assertEqual(self.call("ticket_ending"), "review_pending")
        self.assertTrue(self.call("ticket_review"))
        self.assertEqual(self.state.ticket_records["241"]["public_status"], "Resolvido")
        self.assertEqual(self.call("ticket_ending"), "reviewed")
        self.assertFalse(self.call("ticket_review"))

    def test_team_without_owner_stays_pending_and_can_be_recovered(self):
        self.prepared("peer_review", "team")
        self.assertFalse(self.call("ticket_submit"))
        self.assertEqual(self.call("ticket_ending"), "unowned")
        self.assertTrue(self.call("ticket_summary")["pending"])
        self.call("ticket_handoff", "sabrina")
        self.assertTrue(self.call("ticket_submit"))
        self.assertTrue(self.call("ticket_review"))
        self.assertEqual(self.call("ticket_ending"), "reviewed")

    def test_unavailable_shift_cannot_own_next_step(self):
        self.prepared()
        self.assertFalse(self.call("ticket_handoff", "rodrigo"))
        self.assertEqual(self.state.ticket_owner, "")
        self.assertFalse(self.call("ticket_submit"))
        self.call("ticket_collect", "shift")
        self.assertTrue(self.call("ticket_handoff", "sabrina"))
        self.assertIn("09h", self.state.ticket_next_step)

    def test_policy_change_requires_a_new_explicit_handoff(self):
        self.prepared()
        self.call("ticket_set_policy", "peer_review")
        self.assertEqual(self.state.ticket_owner, "")
        self.assertEqual(self.state.ticket_next_step, "")
        self.assertFalse(self.call("ticket_submit"))

    def test_reopen_requires_reason_and_preserves_resolution_history(self):
        self.prepared()
        self.assertTrue(self.call("ticket_submit"))
        before = copy.deepcopy(self.state.ticket_records["241"])
        self.assertFalse(self.call("ticket_reopen", "   "))
        self.assertEqual(self.state.ticket_records["241"], before)
        self.assertTrue(self.call("ticket_reopen", "A tela continua bloqueada para o turno da noite."))
        record = self.state.ticket_records["241"]
        self.assertEqual(record["public_status"], "Reaberto")
        self.assertEqual(record["public_solution"], before["public_solution"])
        self.assertEqual(record["history"][:len(before["history"])], before["history"])
        self.assertIn("turno da noite", record["history"][-1])
        self.assertEqual(self.call("ticket_ending"), "reopened")
        self.assertFalse(self.call("ticket_followup", "repair"))
        self.assertEqual(self.state.ticket_records["241"]["public_status"], "Reaberto")

    def test_free_reason_cannot_invent_a_verified_repair(self):
        self.prepared()
        self.call("ticket_submit")
        self.call("ticket_reopen", "O problema agora acontece em outro computador.")
        before = copy.deepcopy(self.state.ticket_records)
        self.assertFalse(self.call("ticket_followup", "repair"))
        self.assertEqual(self.state.ticket_records, before)
        self.assertEqual(self.call("ticket_ending"), "reopened")

    def test_explicit_simulated_case_is_the_only_known_repair(self):
        self.prepared()
        self.call("ticket_submit")
        self.assertTrue(self.call("ticket_reopen_simulated_case"))
        self.assertTrue(self.state.ticket_reopen_known_case)
        self.assertIn("turno da noite", self.state.ticket_records["241"]["history"][-1])
        self.assertTrue(self.call("ticket_followup", "repair"))
        self.assertEqual(self.call("ticket_ending"), "repaired")
        self.call("ticket_reopen", "O mesmo texto livre não é avaliação de significado.")
        self.assertFalse(self.state.ticket_reopen_known_case)
        self.assertFalse(self.call("ticket_followup", "repair"))

    def test_confirmed_use_is_written_to_history_once(self):
        self.prepared()
        self.call("ticket_submit")
        previous = list(self.state.ticket_records["241"]["history"])
        self.assertTrue(self.call("ticket_followup", "confirm"))
        history = self.state.ticket_records["241"]["history"]
        self.assertEqual(history[:len(previous)], previous)
        self.assertEqual(len(history), len(previous) + 1)
        self.assertIn("Ana", history[-1])
        self.assertIn("Sabrina", history[-1])
        self.assertFalse(self.call("ticket_followup", "confirm"))
        self.assertEqual(self.state.ticket_records["241"]["history"], history)
        self.assertEqual(self.state.ticket_events.count("followup_confirmed"), 1)

    def test_return_chronology_tracks_recovered_review_and_completed_step(self):
        self.prepared("peer_review", "team")
        self.call("ticket_submit")
        self.call("ticket_handoff", "sabrina")
        self.assertIn("terça-feira às 09h", self.state.ticket_next_step)
        self.call("ticket_submit")
        self.call("ticket_review")
        text = self.call("ticket_return_text")
        self.assertIn("revisão por colega", text)
        self.assertIn("realizada", text)
        self.assertNotIn("Ontem", text)
        self.assertNotIn("amanhã", self.state.ticket_next_step)
        self.assertIn("realizada", self.state.ticket_next_step)
        self.assertNotIn("amanhã", self.call("ticket_summary")["next_step"])

    def test_return_remembers_actual_action_and_pending_next_step(self):
        self.prepared("peer_review", "team")
        self.call("ticket_submit")
        self.assertIn("pendente", self.call("ticket_return_text").lower())
        summary = self.call("ticket_summary")
        self.assertEqual(summary["policy"], "peer_review")
        self.assertEqual(summary["owner"], "")
        self.assertTrue(summary["pending"])
        self.prepared()
        self.call("ticket_submit")
        self.assertIn("public", self.call("ticket_return_text").lower())
        self.assertTrue(self.call("ticket_followup", "confirm"))
        self.assertEqual(self.call("ticket_ending"), "followed_up")


if __name__ == "__main__":
    unittest.main()
