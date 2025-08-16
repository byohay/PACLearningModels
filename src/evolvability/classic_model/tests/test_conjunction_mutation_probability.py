from typing import List, Set, Tuple

import pytest
from pytest_mock.plugin import MockerFixture

from evolvability.classic_model.monotone_conjunction_algorithm.conjunction_mutation_probability import (  # noqa: E501
    ConjunctionMutationProbability,
)


@pytest.fixture
def conjunction_mutation_probability(mocker: MockerFixture) -> ConjunctionMutationProbability:
    """Fixture for ConjunctionMutationProbability with a mocked neighbors_finder."""
    neighbors_finder = mocker.Mock()
    return ConjunctionMutationProbability(neighbors_finder)


@pytest.fixture
def set_return_value_of_get_rep_plus_and_rep_minus(
    conjunction_mutation_probability: ConjunctionMutationProbability,
) -> None:
    """Sets the return value for get_rep_plus_and_rep_minus mock."""
    returned_neighborhood: Set[Tuple[int, ...]] = set()
    returned_neighborhood.add((1, 0, 0, 1))
    returned_neighborhood.add((1, 1, 0, 0))
    returned_neighborhood.add((0, 1, 0, 1))
    returned_neighborhood.add((1, 1, 1, 1))
    conjunction_mutation_probability.neighborhood_finder.get_rep_plus_and_rep_minus.return_value = (
        returned_neighborhood
    )


def test_get_probability_of_rep_from_plus(
    conjunction_mutation_probability: ConjunctionMutationProbability,
    set_return_value_of_get_rep_plus_and_rep_minus: None,  # pylint: disable=W0613
) -> None:
    """Tests the probability calculation for a representation from the plus group."""
    representation: List[int] = [1, 1, 0, 1]

    probability = conjunction_mutation_probability.get_relational_probability(
        representation, (1, 0, 0, 1), 1
    )
    assert probability == 0.125


def test_get_probability_of_rep_from_plus_minus(
    conjunction_mutation_probability: ConjunctionMutationProbability,
    set_return_value_of_get_rep_plus_and_rep_minus: None,  # pylint: disable=W0613
) -> None:
    """Tests the probability calculation when the representation itself is in the plus-minus group."""
    representation: List[int] = [0, 0, 0, 0]

    conjunction_mutation_probability.neighborhood_finder.get_rep_plus_minus.return_value = [
        (0, 0, 0, 0)
    ]

    probability = conjunction_mutation_probability.get_relational_probability(
        representation, (0, 0, 0, 0), 1
    )
    assert probability == 0.5
