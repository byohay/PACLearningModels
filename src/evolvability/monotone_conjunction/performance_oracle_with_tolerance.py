from decimal import Decimal
from typing import Any, Optional, Tuple

from numpy import random


class PerformanceOracleWithTolerance(object):
    """Represents a performance oracle that includes a tolerance parameter."""

    def __init__(self, concept_class: Any, tolerance_param: Decimal):
        """Initializes the PerformanceOracleWithTolerance.
        Args:
            concept_class (Any): The concept class to use for performance calculation.
            tolerance_param (Decimal): The tolerance parameter for performance estimation.
        """
        self.concept_class = concept_class
        self.tolerance_param = tolerance_param

    def get_real_performance(
        self, representation: Tuple[int, ...], conjunction: Optional[Tuple[int, ...]] = None
    ) -> Decimal:
        """Calculates the real performance of a given representation.
        Args:
            representation (Tuple[int, ...]): The representation to evaluate.
            conjunction (Optional[Tuple[int, ...]]): The conjunction to use. Defaults to ideal_function.

        Returns:
            Decimal: The real performance.
        """
        if conjunction is None:
            conjunction = self.concept_class.ideal_function

        union = 0
        intersection = 0
        in_rep_not_in_ideal = 0
        in_ideal_not_in_rep = 0

        for i, j in zip(representation, conjunction):
            if i == 1 or j == 1:
                union += 1

            if i == 1 and j == 1:
                intersection += 1
            elif i == 1 and j == 0:
                in_rep_not_in_ideal += 1
            elif i == 0 and j == 1:
                in_ideal_not_in_rep += 1

        real_perf = (
            Decimal(2**-union)
            + (Decimal(1) - Decimal(2**-intersection))
            + Decimal(2**-intersection)
            * (Decimal(1) - Decimal(2**-in_rep_not_in_ideal))
            * (Decimal(1) - Decimal(2**-in_ideal_not_in_rep))
        )

        return real_perf

    def get_estimated_performance(self, representation: Tuple[int, ...]) -> Decimal:
        """Estimates the performance of a given representation with added tolerance.
        Args:
            representation (Tuple[int, ...]): The representation to estimate.

        Returns:
            Decimal: The estimated performance.
        """
        # Generate a random float and convert it to Decimal with the current context precision
        tolerance = Decimal(
            str(random.uniform(-float(self.tolerance_param), float(self.tolerance_param)))
        )

        real_perf = self.get_real_performance(representation)
        estimated_perf = tolerance + real_perf

        return max(Decimal(-1), min(Decimal(1), estimated_perf))
