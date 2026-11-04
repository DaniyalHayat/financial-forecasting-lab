import copy
import unittest
import finance


class RollingTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):cls.history=finance.build()['actuals']

    def test_horizon_advances_after_new_actual(self):
        history=copy.deepcopy(self.history)
        new=copy.deepcopy(history[-1]);new['month']='2026-07';history.append(new)
        result=finance.forecast(history)
        self.assertEqual(result[0]['month'],'2026-08')
        self.assertEqual(result[-1]['month'],'2027-07')
        self.assertEqual(len(result),12)

    def test_gap_duplicate_or_reverse_months_fail(self):
        for mutate in [lambda h:h.reverse(), lambda h:h.__setitem__(3,h[2])]:
            history=copy.deepcopy(self.history);mutate(history)
            with self.assertRaises(ValueError):finance.forecast(history)
