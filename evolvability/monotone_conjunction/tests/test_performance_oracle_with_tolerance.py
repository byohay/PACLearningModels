import unittest
from unittest.mock import Mock
from decimal import Decimal

from evolvability.monotone_conjunction.performance_oracle_with_tolerance import (
    PerformanceOracleWithTolerance,
)


class TestPerformanceOracleWithTolerance(unittest.TestCase):
    def setUp(self):
        self.tolerance_param = Decimal("0.00001")
        self.concept_class = Mock()
        self.perf = PerformanceOracleWithTolerance(self.concept_class, self.tolerance_param)

    def test_one_perf_example(self):

        self.concept_class.ideal_function = (0, 1, 0, 0, 1)

        expected_value = Decimal("0.125") * Decimal("6")
        actual_value = self.perf.get_estimated_performance((0, 0, 1, 0, 1))

        self.assertAlmostEqual(expected_value, actual_value, delta=self.tolerance_param)
