from typing import Any, Callable, Set, Tuple, List

import pytest
from pytest_mock.plugin import MockerFixture

from evolvability.classic_model.mutator import Mutator


@pytest.fixture
def mutator_mocks(mocker: MockerFixture) -> Tuple[Any, Any, Any, Any]:
    """Fixture for mocked components of the Mutator."""
    neighborhood = mocker.Mock()
    performance = mocker.Mock()
    tolerance = mocker.Mock()
    mutation_probability = mocker.Mock()
    mutation_probability.get_relational_probability.return_value = 0.2
    tolerance.get_tolerance.return_value = 2**-5
    return neighborhood, performance, tolerance, mutation_probability


@pytest.fixture
def mutator(mutator_mocks: Tuple[Any, Any, Any, Any]) -> Mutator:
    """Fixture for the Mutator instance."""
    neighborhood, performance, tolerance, mutation_probability = mutator_mocks
    epsilon = 1
    return Mutator(neighborhood, performance, tolerance, mutation_probability, epsilon)


@pytest.fixture
def set_neighborhood(mutator: Mutator) -> Callable[[Tuple[int, ...]], None]:
    """Fixture to set the return value for get_neighborhood_of_rep mock."""

    def _set_neighborhood(expected_rep: Tuple[int, ...]) -> None:
        neighborhood_set: Set[Tuple[int, ...]] = set()
        neighborhood_set.add(expected_rep)
        neighborhood_set.add((1, 1, 0, 0))
        neighborhood_set.add((1, 0, 0, 1))
        mutator.neighborhood.get_neighborhood_of_rep.return_value = neighborhood_set

    return _set_neighborhood


def test_mutator__one_in_bene(
    mutator: Mutator,
    mutator_mocks: Tuple[Any, Any, Any, Any],
    set_neighborhood: Callable[[Tuple[int, ...]], None],
) -> None:
    """Tests the evolutionary step when one beneficial mutation exists."""
    _, performance, tolerance, _ = mutator_mocks
    representation: Tuple[int, ...] = (1, 1, 0, 1)
    perf_of_representation = 0.2
    expected_rep: Tuple[int, ...] = (1, 1, 1, 1)
    perf_of_expected_representation = perf_of_representation + tolerance.get_tolerance.return_value

    def perf_returns(rep_val: Tuple[int, ...]) -> float:
        if rep_val == representation:
            return perf_of_representation
        if rep_val == expected_rep:
            return perf_of_expected_representation
        return 0.0

    set_neighborhood(expected_rep)
    performance.get_estimated_performance.side_effect = perf_returns

    assert mutator.evolutionary_step(representation) == expected_rep


def test_mutator__two_in_neut(
    mutator: Mutator,
    mutator_mocks: Tuple[Any, Any, Any, Any],
) -> None:
    """Tests the evolutionary step when two neutral mutations exist."""
    _, performance, _, _ = mutator_mocks
    representation: Tuple[int, ...] = (1, 1, 0, 1)
    expected_reps: Set[Tuple[int, ...]] = set()
    expected_reps.add((1, 1, 1, 1))
    expected_reps.add((0, 0, 0, 0))

    performance.get_estimated_performance.return_value = 0.0
    mutator.neighborhood.get_neighborhood_of_rep.return_value = expected_reps

    assert mutator.evolutionary_step(representation) in expected_reps
