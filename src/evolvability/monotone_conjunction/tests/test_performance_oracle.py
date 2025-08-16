from typing import Any, List

import pytest
from pytest_mock.plugin import MockerFixture

from evolvability.monotone_conjunction.performance_oracle import PerformanceOracle


@pytest.fixture
def performance_oracle_mocks(mocker: MockerFixture) -> Any:
    """Fixture for mocked concept_class."""
    concept_class = mocker.Mock()
    concept_class.get_random_sample.return_value = [1, -1, 1]
    return concept_class


@pytest.fixture
def performance_oracle(performance_oracle_mocks: Any) -> PerformanceOracle:
    """Fixture for the PerformanceOracle instance."""
    selection_size = 5
    return PerformanceOracle(performance_oracle_mocks, selection_size)


def test_simple_perf(
    performance_oracle: PerformanceOracle,
    performance_oracle_mocks: Any,
) -> None:
    """Tests the simple performance estimation."""
    performance_oracle_mocks.is_function_answering_yes_on_sample.side_effect = [
        True,
        True,
        False,
        False,
        True,
        False,
        False,
        True,
        True,
        False,
    ]

    representation: List[int] = [1, 0, 0]

    assert performance_oracle.get_estimated_performance(representation) == 0.4
