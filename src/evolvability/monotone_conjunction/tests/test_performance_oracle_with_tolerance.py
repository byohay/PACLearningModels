from decimal import Decimal
from typing import Any, Tuple

import pytest
from pytest_mock.plugin import MockerFixture

from evolvability.monotone_conjunction.performance_oracle_with_tolerance import (
    PerformanceOracleWithTolerance,
)


@pytest.fixture
def performance_oracle_with_tolerance_mocks(mocker: MockerFixture) -> Any:
    """Fixture for mocked concept_class."""
    concept_class = mocker.Mock()
    return concept_class


@pytest.fixture
def performance_oracle_with_tolerance(
    performance_oracle_with_tolerance_mocks: Any,
) -> PerformanceOracleWithTolerance:
    """Fixture for the PerformanceOracleWithTolerance instance."""
    tolerance_param = Decimal("0.00001")
    return PerformanceOracleWithTolerance(performance_oracle_with_tolerance_mocks, tolerance_param)


def test_one_perf_example(
    performance_oracle_with_tolerance: PerformanceOracleWithTolerance,
    performance_oracle_with_tolerance_mocks: Any,
) -> None:
    """Tests a simple performance estimation example with tolerance."""
    performance_oracle_with_tolerance_mocks.ideal_function = (0, 1, 0, 0, 1)

    expected_value = Decimal("0.125") * Decimal("6")
    representation: Tuple[int, ...] = (0, 0, 1, 0, 1)
    actual_value = performance_oracle_with_tolerance.get_estimated_performance(representation)

    assert actual_value == pytest.approx(
        expected_value, rel=performance_oracle_with_tolerance.tolerance_param
    )
