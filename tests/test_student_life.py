"""Regras da agenda opcional, sem iniciar o renderizador Ren'Py."""
import copy
import pathlib
import textwrap
import types
import unittest

SOURCE = pathlib.Path(__file__).resolve().parents[1] / 'scripts/student_life.rpy'


def load_state():
    state = types.SimpleNamespace()
    api = {'store': state}
    source = SOURCE.read_text(encoding='utf-8')
    for line in source.splitlines():
        if line.startswith('default '):
            name, value = line[8:].split(' = ', 1)
            setattr(state, name, eval(value))
    code = source.split('init python:\n', 1)[1].split('\nscreen ', 1)[0]
    exec(compile(textwrap.dedent(code), str(SOURCE), 'exec'), api)
    return state, api


class StudentLifeTests(unittest.TestCase):
    def setUp(self):
        self.assertTrue(SOURCE.exists(), 'O módulo opcional precisa existir')
        self.state, self.api = load_state()

    def call(self, name, *args):
        return self.api[name](*args)

    def test_conflict_preserves_commitment_until_player_reorganizes(self):
        self.assertTrue(self.call('student_assign', 'thursday', 'rest'))
        before = copy.deepcopy(self.state.student_schedule)
        self.assertFalse(self.call('student_assign', 'thursday', 'workshop'))
        self.assertEqual(self.state.student_schedule, before)
        self.assertIn('libere', self.state.student_feedback.lower())
        self.assertTrue(self.call('student_clear', 'thursday'))
        self.assertTrue(self.call('student_assign', 'thursday', 'workshop'))

    def test_availability_and_explicit_local_study_renegotiation(self):
        self.assertFalse(self.call('student_assign', 'tuesday', 'workshop'))
        self.assertFalse(self.call('student_assign', 'thursday', 'study'))
        self.assertTrue(self.call('student_renegotiate_study'))
        self.assertEqual(self.state.student_schedule, {'tuesday': None, 'thursday': None})
        self.assertTrue(self.call('student_assign', 'thursday', 'study'))
        self.assertEqual(self.state.student_schedule['tuesday'], None)

    def test_rest_and_no_overtime_have_concrete_agreement_without_penalty(self):
        self.call('student_assign', 'tuesday', 'rest')
        self.call('student_assign', 'thursday', 'rest')
        self.assertTrue(self.call('student_agree'))
        agreement = self.state.student_agreement
        self.assertIn('horário regular', agreement)
        self.assertIn('colega', agreement)
        self.assertEqual(self.state.student_schedule, {'tuesday': 'rest', 'thursday': 'rest'})
        self.call('student_clear', 'thursday')
        self.call('student_assign', 'thursday', 'overtime')
        self.assertTrue(self.call('student_agreement_pending'))
        self.call('student_agree')
        self.assertIn('quinta', self.state.student_agreement.lower())
        self.assertFalse(self.call('student_agreement_pending'))

    def test_optional_course_requires_available_workshop_and_keeps_tip(self):
        self.assertFalse(self.call('student_take_course'))
        self.call('student_assign', 'thursday', 'workshop')
        self.assertFalse(self.call('student_take_course'))
        self.call('student_visit', 'workshop')
        self.assertTrue(self.call('student_take_course'))
        self.assertFalse(self.call('student_clear', 'thursday'))
        self.assertFalse(self.call('student_assign', 'thursday', 'overtime'))
        self.assertEqual(self.state.student_schedule['thursday'], 'workshop')
        self.assertIn('concluída', self.state.student_feedback.lower())
        self.assertTrue(self.call('student_assign', 'tuesday', 'rest'))
        self.assertTrue(self.call('student_clear', 'tuesday'))
        self.assertTrue(self.call('student_assign', 'tuesday', 'study'))
        self.assertTrue(self.state.student_course_done)
        self.assertIn('usabilidade', self.call('student_summary').lower())
        self.assertIn('cancelar', self.api['STUDENT_TIP'].lower())

    def test_visits_and_evidence_are_idempotent_and_reset_is_scoped(self):
        self.state.campaign_results = {'lab': {'summary': 'Entregue'}}
        self.call('student_visit', 'campus')
        self.call('student_visit', 'campus')
        self.call('student_inspect', 'campus')
        self.call('student_inspect', 'campus')
        self.assertFalse(self.call('student_visit', 'unknown'))
        self.assertFalse(self.call('student_inspect', 'unknown'))
        self.assertEqual(self.state.student_visits, ['campus'])
        self.assertEqual(self.state.student_evidence, ['campus'])
        self.assertIn('Campus', self.call('student_summary'))
        self.call('student_reset')
        self.assertEqual(self.state.student_visits, [])
        self.assertEqual(self.state.student_evidence, [])
        self.assertEqual(self.state.campaign_results, {'lab': {'summary': 'Entregue'}})

    def test_invalid_inputs_do_not_replace_valid_agenda(self):
        self.call('student_assign', 'tuesday', 'study')
        before = copy.deepcopy(self.state.student_schedule)
        for slot, activity in [('friday', 'rest'), ('tuesday', 'unknown')]:
            self.assertFalse(self.call('student_assign', slot, activity))
        self.assertFalse(self.call('student_clear', 'friday'))
        self.assertEqual(self.state.student_schedule, before)

    def test_location_clock_uses_visit_or_reserved_activity_without_changing_agenda(self):
        self.assertIn('student_location_clock', self.api)
        self.assertEqual(self.call('student_location_clock', 'campus'), ('Visita ao campus', '16h', 'day'))
        self.assertEqual(self.call('student_location_clock', 'workshop'), ('Visita à oficina', '16h', 'day'))
        self.call('student_assign', 'tuesday', 'study')
        self.assertEqual(self.call('student_location_clock', 'campus'), ('Terça-feira', '20h', 'night'))
        self.call('student_clear', 'tuesday')
        self.call('student_renegotiate_study')
        self.call('student_assign', 'thursday', 'study')
        self.assertEqual(self.call('student_location_clock', 'campus'), ('Quinta-feira', '20h', 'night'))
        self.call('student_clear', 'thursday')
        self.call('student_assign', 'thursday', 'workshop')
        self.assertEqual(self.call('student_location_clock', 'workshop'), ('Visita à oficina', '16h', 'day'))
        self.call('student_visit', 'workshop')
        self.call('student_take_course')
        self.assertEqual(self.call('student_location_clock', 'workshop'), ('Quinta-feira', '20h', 'night'))
        self.assertEqual(self.state.student_schedule, {'tuesday': None, 'thursday': 'workshop'})


if __name__ == '__main__':
    unittest.main()
