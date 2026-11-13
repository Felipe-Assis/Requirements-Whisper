"""Notebook mail is a read-only view of actual campaign facts."""
import copy
import pathlib
import textwrap
import types
import unittest


ROOT = pathlib.Path(__file__).resolve().parents[1]
SOURCE = ROOT / "scripts/notebook_desktop.rpy"


class NotebookDesktopTests(unittest.TestCase):
    def setUp(self):
        self.assertTrue(SOURCE.exists(), "The notebook desktop must exist")
        self.state = types.SimpleNamespace(
            notebook_read=[], campaign_results={}, campaign_clock={}, campaign_started_projects=[],
            lab_active=False, lab_evidence=[], exp_sources=[], ticket_evidence=[],
            ticket_records={}, ticket_selected="241", student_agreement="",
            student_agreed_schedule={}, student_schedule={},
        )
        self.api = {"store": self.state}
        student = (ROOT / "scripts/student_life.rpy").read_text(encoding="utf-8")
        exec(textwrap.dedent(student.split("init python:\n", 1)[1].split("\nscreen ", 1)[0]), self.api)
        campaign = (ROOT / "scripts/campaign_state.rpy").read_text(encoding="utf-8")
        exec(textwrap.dedent(campaign.split("init python:\n", 1)[1]), self.api)
        source = SOURCE.read_text(encoding="utf-8")
        code = source.split("init python:\n", 1)[1].split("\nscreen ", 1)[0]
        exec(compile(textwrap.dedent(code), str(SOURCE), "exec"), self.api)

    def messages(self):
        return self.api["notebook_messages"]()

    def test_invites_are_stable_and_reading_changes_only_read_ids(self):
        before = copy.deepcopy(vars(self.state))
        messages = self.messages()
        self.assertEqual({m["id"] for m in messages}, {"invite_lab", "invite_expenses", "invite_tickets"})
        self.assertTrue(self.api["notebook_mark_read"]("invite_lab"))
        self.assertTrue(self.api["notebook_mark_read"]("invite_lab"))
        self.assertFalse(self.api["notebook_mark_read"]("unknown"))
        self.assertEqual(self.state.notebook_read, ["invite_lab"])
        for name, value in before.items():
            if name != "notebook_read":
                self.assertEqual(getattr(self.state, name), value)

    def test_two_returns_keep_distinct_real_outcomes_without_inventing_delivery(self):
        self.state.campaign_results = {
            "lab": {"outcome": "waiting", "summary": "A agenda ainda não foi entregue.", "pending": "Pedir autorização."},
            "expenses": {"outcome": "delivered", "summary": "Cancelamento e desfazer conferidos.", "pending": "Acompanhar com Lia."},
        }
        before = copy.deepcopy(self.state.campaign_results)
        returns = {m["project"]: m for m in self.messages() if m["kind"] == "return"}
        self.assertEqual(set(returns), {"lab", "expenses"})
        self.assertIn("A agenda ainda não foi entregue.", returns["lab"]["body"])
        self.assertIn("Pedir autorização.", returns["lab"]["body"])
        self.assertIn("Cancelamento e desfazer conferidos.", returns["expenses"]["body"])
        self.assertNotEqual(returns["lab"]["id"], returns["expenses"]["id"])
        self.assertEqual(self.state.campaign_results, before)

    def test_changed_return_is_unread_and_prior_read_id_survives(self):
        self.state.campaign_results = {"lab": {"outcome": "waiting", "summary": "Pesquisa pendente", "pending": "Autorização"}}
        first = next(m for m in self.messages() if m["kind"] == "return")
        self.api["notebook_mark_read"](first["id"])
        self.state.campaign_results["lab"]["summary"] = "Pesquisa devolvida; entrega continua pendente"
        second = next(m for m in self.messages() if m["kind"] == "return")
        self.assertNotEqual(first["id"], second["id"])
        self.assertIn(first["id"], self.state.notebook_read)
        self.assertNotIn(second["id"], self.state.notebook_read)
        self.assertEqual(second["id"], next(m for m in self.messages() if m["kind"] == "return")["id"])

    def test_demands_agreement_and_logs_follow_existing_facts(self):
        self.state.campaign_clock = {"place": "startup", "day": "Início da jornada"}
        self.assertFalse(any(m["kind"] == "demand" for m in self.messages()))
        self.state.lab_active = True
        self.state.student_agreement = "Revisão no horário regular."
        self.state.student_agreed_schedule = {"tuesday": "study"}
        self.state.student_schedule = {"tuesday": "rest"}
        self.state.ticket_records = {"241": {"history": ["14h10 · Atendimento iniciado."]}}
        self.state.ticket_evidence = ["log"]
        self.state.ticket_active = True
        self.state.campaign_started_projects = ["lab", "tickets"]
        messages = self.messages()
        self.assertIn("demand_lab", {m["id"] for m in messages})
        self.assertIn("demand_tickets", {m["id"] for m in messages})
        agreement = next(m for m in messages if m["kind"] == "agreement")
        self.assertIn("Revisão no horário regular.", agreement["body"])
        self.assertIn("agenda mudou", agreement["body"])
        history = next(m for m in messages if m["kind"] == "history")
        self.assertIn("14h10 · Atendimento iniciado.", history["body"])
        self.assertNotIn("Resolvido", history["body"])

    def test_old_module_evidence_does_not_start_projects_after_campaign_reset(self):
        self.state.lab_evidence = ["sheets"]
        self.state.exp_sources = ["receipt"]
        self.state.ticket_evidence = ["log"]
        self.assertFalse(any(message["kind"] == "demand" for message in self.messages()))

    def test_shared_room_and_old_active_flags_do_not_create_demands(self):
        self.state.lab_active = True
        self.state.ticket_active = True
        for milestone in ("Conversa com Sabrina", "Planejamento do laboratório", "Visita à mesa da equipe"):
            self.state.campaign_clock = {"place": "startup", "day": milestone}
            self.assertFalse(any(message["kind"] == "demand" for message in self.messages()))

    def test_explicit_start_is_idempotent_and_campaign_reset_clears_it(self):
        self.assertIn("campaign_mark_started", self.api)
        self.assertTrue(self.api["campaign_mark_started"]("expenses"))
        self.assertTrue(self.api["campaign_mark_started"]("expenses"))
        self.assertFalse(self.api["campaign_mark_started"]("unknown"))
        self.assertEqual(self.state.campaign_started_projects, ["expenses"])
        demands = [message["id"] for message in self.messages() if message["kind"] == "demand"]
        self.assertEqual(demands, ["demand_expenses"])
        self.api["campaign_reset"]()
        self.assertEqual(self.state.campaign_started_projects, [])
        self.assertFalse(any(message["kind"] == "demand" for message in self.messages()))


if __name__ == "__main__":
    unittest.main()
