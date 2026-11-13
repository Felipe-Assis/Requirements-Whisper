"""Rules exercised without the Ren'Py renderer; UI journeys live in expenses.rpy."""
import copy
import pathlib
import textwrap
import types
import unittest

SOURCE = pathlib.Path(__file__).resolve().parents[1] / 'scripts/expenses_state.rpy'

def load_state():
    store = types.SimpleNamespace()
    namespace = {'store': store}
    if not SOURCE.exists():
        return store, namespace
    source = SOURCE.read_text(encoding='utf-8')
    for line in source.splitlines():
        if line.startswith('default '):
            name, value = line[8:].split(' = ', 1)
            setattr(store, name, eval(value))
    exec(compile(textwrap.dedent(source.split('init python:\n', 1)[1]), str(SOURCE), 'exec'), namespace)
    return store, namespace

class ExpensesTests(unittest.TestCase):
    def setUp(self):
        self.assertTrue(SOURCE.exists(), 'Expense campaign rules must exist')
        self.state, self.api = load_state()
        self.call('exp_reset')

    def call(self, name, *args):
        return self.api[name](*args)

    def build(self):
        self.call('exp_set_plan', 'core')
        for change in ('defer', 'total', 'undo'):
            self.call('exp_apply_change', change)
        self.assertTrue(self.call('exp_build', 'pair'))

    def test_legacy_cancel_reproduces_real_data_loss_then_build_resets_fixture(self):
        self.assertEqual(self.call('exp_total'), 10000)
        self.call('exp_request_delete', 'meal18')
        self.assertEqual(self.call('exp_total'), 8000)
        self.call('exp_cancel_delete')
        self.assertEqual(self.call('exp_total'), 8000)
        self.assertTrue(self.state.exp_before_reproduced)
        self.build()
        self.assertEqual(self.call('exp_total'), 10000)
        self.assertTrue(self.state.exp_before_reproduced)

    def test_confirmation_cancel_is_idempotent_and_preserves_exact_rows(self):
        self.build()
        original = copy.deepcopy(self.state.exp_rows)
        self.assertTrue(self.call('exp_request_delete', 'meal18'))
        self.assertEqual(self.state.exp_rows, original)
        self.assertFalse(self.call('exp_request_delete', 'bus'))
        self.call('exp_cancel_delete')
        self.call('exp_cancel_delete')
        self.assertEqual(self.state.exp_rows, original)
        self.assertEqual(self.call('exp_total'), 10000)
        self.assertFalse(self.call('exp_confirm_delete'))

    def test_confirm_removes_only_selected_id_and_recalculates(self):
        self.build()
        self.call('exp_request_delete', 'meal18')
        self.assertTrue(self.call('exp_confirm_delete'))
        self.assertEqual(self.call('exp_total'), 8000)
        self.assertEqual([row['id'] for row in self.state.exp_rows], ['meal17', 'book', 'bus'])
        self.assertFalse(self.call('exp_confirm_delete'))
        self.assertEqual(self.call('exp_total'), 8000)

    def test_undo_restores_copy_without_aliasing_or_repeated_reversion(self):
        self.build()
        original = copy.deepcopy(self.state.exp_rows)
        self.call('exp_request_delete', 'meal18')
        self.call('exp_confirm_delete')
        undo_snapshot = self.state.exp_undo_rows
        self.assertTrue(self.call('exp_undo'))
        undo_snapshot[0]['amount'] = 1
        self.assertEqual(self.state.exp_rows, original)
        self.assertFalse(self.call('exp_undo'))
        self.assertEqual(self.call('exp_total'), 10000)
        self.assertIn('undo', self.state.exp_checks)

    def test_equal_values_are_not_duplicate_detection(self):
        self.build()
        self.call('exp_request_delete', 'bus')
        self.call('exp_confirm_delete')
        self.assertEqual(self.call('exp_total'), 8000)
        self.assertFalse(self.call('exp_demo_ready'))
        self.assertTrue(any(row['id'] == 'meal18' for row in self.state.exp_rows))
        self.call('exp_undo')
        self.assertTrue(self.state.exp_recovered)

    def test_edit_rejects_zero_negative_boolean_and_recalculates_positive(self):
        self.build()
        original = copy.deepcopy(self.state.exp_rows)
        for amount in (0, -1, True, '30', None):
            self.assertFalse(self.call('exp_edit', 'bus', amount))
            self.assertEqual(self.state.exp_rows, original)
        self.assertTrue(self.state.exp_zero_rejected)
        self.assertTrue(self.call('exp_edit', 'bus', 3000))
        self.assertEqual(self.call('exp_total'), 11000)
        self.assertTrue(self.state.exp_sidequest)
        self.call('exp_undo')
        self.assertEqual(self.call('exp_total'), 10000)

    def test_evidence_and_demo_are_needed_for_delivery(self):
        self.build()
        self.assertFalse(self.call('exp_deliver'))
        for source in ('receipt', 'ledger', 'lia'):
            self.call('exp_inspect', source)
        self.call('exp_request_delete', 'meal18')
        self.call('exp_cancel_delete')
        self.call('exp_request_delete', 'meal18')
        self.call('exp_confirm_delete')
        self.call('exp_undo')
        self.call('exp_request_delete', 'meal18')
        self.call('exp_confirm_delete')
        self.assertTrue(self.call('exp_demo_ready'))
        self.assertTrue(self.call('exp_deliver'))
        self.assertTrue(self.state.exp_delivered)
        self.assertEqual(self.call('exp_outcome'), 'reliable')

    def test_bank_research_is_not_delivery_and_invalid_actions_preserve_decision(self):
        self.assertTrue(self.call('exp_set_plan', 'bank'))
        self.assertFalse(self.call('exp_set_plan', 'unknown'))
        self.assertFalse(self.call('exp_build', 'pair'))
        self.assertFalse(self.call('exp_deliver'))
        self.assertEqual(self.call('exp_outcome'), 'waiting')
        self.assertEqual(self.state.exp_plan, 'bank')
        self.assertTrue(self.call('exp_set_plan', 'core'))
        self.assertTrue(self.state.exp_renegotiated)

    def test_empty_total_and_bad_ids_never_mutate(self):
        self.build()
        original = copy.deepcopy(self.state.exp_rows)
        self.assertFalse(self.call('exp_request_delete', 'unknown'))
        self.assertFalse(self.call('exp_edit', 'unknown', 2000))
        self.assertEqual(self.state.exp_rows, original)
        self.state.exp_rows = []
        self.assertEqual(self.call('exp_total'), 0)
        self.assertEqual(self.call('exp_money', 0), 'R$ 0,00')
        self.assertEqual(self.call('exp_money', 8000), 'R$ 80,00')

    def test_two_legitimate_removals_can_restart_the_corrected_sandbox(self):
        self.build()
        for source in ('receipt', 'ledger', 'lia'):
            self.call('exp_inspect', source)
        for row_id in ('bus', 'book'):
            self.call('exp_request_delete', row_id)
            self.call('exp_confirm_delete')
        self.call('exp_undo')
        self.assertFalse(any(row['id'] == 'bus' for row in self.state.exp_rows))
        self.assertFalse(self.call('exp_demo_ready'))
        self.call('exp_restore_fixture')
        self.assertEqual(self.state.exp_rows, self.api['exp_fixture']())
        self.assertEqual(self.state.exp_checks, [])
        self.assertTrue(self.state.exp_built)
        self.assertEqual(self.state.exp_reviewer, 'pair')
        self.assertEqual(set(self.state.exp_sources), {'receipt', 'ledger', 'lia'})
        self.call('exp_request_delete', 'meal18')
        self.call('exp_cancel_delete')
        self.call('exp_request_delete', 'meal18')
        self.call('exp_confirm_delete')
        self.call('exp_undo')
        self.call('exp_request_delete', 'meal18')
        self.call('exp_confirm_delete')
        self.assertTrue(self.call('exp_demo_ready'))
        self.assertTrue(self.call('exp_deliver'))

    def test_result_keeps_independent_rows_for_the_product_preview(self):
        result = self.call('exp_result')
        self.assertEqual(result['rows'], self.state.exp_rows)
        result['rows'][0]['amount'] = 1
        result['rows'].pop()
        self.assertEqual(self.call('exp_total'), 10000)
        self.assertEqual(len(self.state.exp_rows), 4)

    def test_reset_only_resets_expenses_and_collection_is_idempotent(self):
        self.state.player_name = 'Pat'
        self.state.campaign_results = {'lab': {'outcome': 'reliable'}}
        self.call('exp_inspect', 'receipt')
        self.call('exp_inspect', 'receipt')
        self.assertEqual(self.state.exp_sources, ['receipt'])
        self.assertFalse(self.call('exp_inspect', 'unknown'))
        self.call('exp_reset')
        self.assertEqual(self.state.exp_sources, [])
        self.assertEqual(self.call('exp_total'), 10000)
        self.assertEqual(self.state.player_name, 'Pat')
        self.assertEqual(self.state.campaign_results, {'lab': {'outcome': 'reliable'}})

if __name__ == '__main__':
    unittest.main()
