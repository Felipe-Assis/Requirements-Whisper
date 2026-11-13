import pathlib
import textwrap
import types
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[1]

def load_state():
    state = types.SimpleNamespace()
    api = {'store': state, 'student_reset': lambda: None}
    for name in ('campaign_state.rpy', 'app_builder_state.rpy'):
        source = (ROOT / 'scripts' / name).read_text(encoding='utf-8')
        for line in source.splitlines():
            if line.startswith('default '):
                key, value = line[8:].split(' = ', 1)
                setattr(state, key, eval(value))
        exec(textwrap.dedent(source.split('init python:\n', 1)[1]), api)
    return state, api

class CampaignTests(unittest.TestCase):
    def setUp(self):
        self.state, self.api = load_state()

    def test_results_are_independent_snapshots(self):
        result = {'summary': 'Entregue', 'facts': ['fonte']}
        self.api['campaign_record']('lab', result)
        result['facts'].append('inventada')
        self.api['campaign_record']('expenses', {'summary': 'Em revisão'})
        self.assertEqual(self.state.campaign_results['lab']['facts'], ['fonte'])
        self.api['campaign_record']('lab', {'summary': 'Reparado'})
        self.assertEqual(len(self.state.campaign_results), 2)
        self.assertEqual(self.state.campaign_results['expenses']['summary'], 'Em revisão')

    def test_reorder_is_swap_and_result_retains_built_layout(self):
        self.api['campaign_place_module']('expenses', 'records', 0)
        self.assertEqual(self.api['campaign_layout']('expenses'), ['records', 'balance', 'actions'])
        self.api['campaign_record']('expenses', {'summary': 'Entregue'})
        self.api['campaign_place_module']('expenses', 'actions', 0)
        self.assertEqual(self.state.campaign_results['expenses']['layout'], ['records', 'balance', 'actions'])
        self.assertEqual(set(self.api['campaign_layout']('expenses')), {'records', 'balance', 'actions'})

    def test_invalid_drop_cannot_remove_module(self):
        initial = self.api['campaign_layout']('expenses')
        for module, slot in [('unknown', 0), ('balance', -1), ('records', 3)]:
            self.assertFalse(self.api['campaign_place_module']('expenses', module, slot))
        self.assertEqual(initial, self.api['campaign_layout']('expenses'))

    def test_memory_does_not_expose_mutable_snapshot(self):
        self.api['campaign_record']('lab', {'facts': ['sheets']})
        memory = self.api['campaign_memory']('lab')
        memory['facts'].clear()
        self.assertEqual(self.state.campaign_results['lab']['facts'], ['sheets'])
        self.assertEqual(self.api['campaign_memory']('unknown'), {})

if __name__ == '__main__':
    unittest.main()
