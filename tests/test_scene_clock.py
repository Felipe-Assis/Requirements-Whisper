import pathlib
import textwrap
import types
import unittest

class SceneClockTests(unittest.TestCase):
    def setUp(self):
        self.state = types.SimpleNamespace(campaign_clock={})
        self.api = {'store': self.state}
        source = pathlib.Path(__file__).resolve().parents[1] / 'scripts/scene_clock.rpy'
        exec(textwrap.dedent(source.read_text(encoding='utf-8').split('init python:\n', 1)[1]), self.api)

    def test_same_room_uses_explicit_time_and_light(self):
        self.api['campaign_set_clock']('support', 'Segunda-feira', '14h30', 'day')
        self.assertEqual(self.state.campaign_clock['image'], 'images/bg/suporte_dia.png')
        self.api['campaign_set_clock']('support', 'Terça-feira', '09h', 'morning')
        self.assertEqual(self.state.campaign_clock['image'], 'images/bg/suporte_manha.png')
        self.api['campaign_set_clock']('support', 'Semana seguinte', '10h10', 'rain')
        self.assertIn('chuva', self.api['campaign_clock_caption']())
        self.assertEqual(self.state.campaign_clock['image'], 'images/bg/suporte_chuva.png')

    def test_unknown_variant_cannot_desynchronize_clock_and_image(self):
        self.api['campaign_set_clock']('campus', 'Terça-feira', '20h', 'night')
        before = dict(self.state.campaign_clock)
        with self.assertRaises(ValueError):
            self.api['campaign_set_clock']('campus', 'Terça-feira', '20h', 'rain')
        self.assertEqual(self.state.campaign_clock, before)

    def test_project_order_does_not_invent_a_global_week(self):
        self.api['campaign_set_clock']('startup', 'Retorno · semana seguinte', '09h', 'morning')
        self.api['campaign_set_clock']('lab', 'Segunda-feira · início do caso', '14h', 'afternoon')
        self.assertIn('início do caso', self.api['campaign_clock_caption']())
        self.assertEqual(self.state.campaign_clock['image'], 'images/bg/laboratorio.png')
