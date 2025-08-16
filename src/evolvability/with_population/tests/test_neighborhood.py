from typing import Callable, Tuple, Any

import pytest
from pytest_mock.plugin import MockerFixture

from evolvability.with_population.neighborhood import (
    NeighborhoodWithOtherRepresentations,
)


@pytest.fixture
def neighborhood_mocks(mocker: MockerFixture) -> Tuple[Any, Any, Callable[..., Any]]:
    """Fixture for mocked mutation_neighborhood and natural_process."""
    mutation_neighborhood = mocker.Mock()
    natural_process = mocker.Mock()

    def return_itself(*args: Any) -> Any:
        return args[0]

    mutation_neighborhood.get_neighborhood_of_rep.side_effect = return_itself
    natural_process.get_a_mutation_from_the_reps.side_effect = return_itself
    return mutation_neighborhood, natural_process, return_itself


@pytest.fixture
def setup_neighborhood_calc(
    neighborhood_mocks: Tuple[Any, Any, Callable[..., Any]],
) -> Callable[[int], NeighborhoodWithOtherRepresentations]:
    """Fixture to set up NeighborhoodWithOtherRepresentations with different mutation factors."""
    mutation_neighborhood, natural_process, _ = neighborhood_mocks

    def _setup(mutation_factor: int) -> NeighborhoodWithOtherRepresentations:
        return NeighborhoodWithOtherRepresentations(
            2, # number_of_activations
            mutation_neighborhood,
            mutation_factor,
            natural_process,
        )

    return _setup


def test_no_mutation(
    setup_neighborhood_calc: Callable[[int], NeighborhoodWithOtherRepresentations],
    neighborhood_mocks: Tuple[Any, Any, Callable[..., Any]],
) -> None:
    """Tests that no mutation occurs when the mutation factor is zero."""
    mutation_neighborhood, _, _ = neighborhood_mocks
    neighborhood_calc = setup_neighborhood_calc(0)

    first_rep = (1, 3, 5)
    second_rep = (2, 4, 6)

    neighborhood_calc.get_neighborhood(first_rep, second_rep)

    assert mutation_neighborhood.get_neighborhood_of_rep.call_count == 0


def test_mutation_called_based_on_mutation_factor(
    setup_neighborhood_calc: Callable[[int], NeighborhoodWithOtherRepresentations],
    neighborhood_mocks: Tuple[Any, Any, Callable[..., Any]],
) -> None:
    """Tests that mutation is called based on the mutation factor."""
    mutation_neighborhood, _, _ = neighborhood_mocks
    neighborhood_calc = setup_neighborhood_calc(1)

    first_rep = (1, 3, 5)
    second_rep = (2, 4, 6)

    neighborhood_calc.get_neighborhood(first_rep, second_rep)

    assert mutation_neighborhood.get_neighborhood_of_rep.call_count == 2 # number_of_activations is 2
