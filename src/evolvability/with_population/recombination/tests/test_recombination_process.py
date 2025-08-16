from typing import Tuple

import pytest

from evolvability.with_population.recombination.recombination_process import (
    RecombinationProcess,
)


@pytest.fixture
def recombination_process() -> RecombinationProcess:
    """Fixture for RecombinationProcess."""
    return RecombinationProcess()


def test_get_recomb_of_two_reps_without_mutation(
    recombination_process: RecombinationProcess,
) -> None:
    """Tests the recombination of two representations without mutation."""
    first_rep: Tuple[int, ...] = (1, 3, 5)
    second_rep: Tuple[int, ...] = (2, 4, 6)

    desc_rep: Tuple[int, ...] = recombination_process.get_a_mutation_from_the_reps(
        first_rep, second_rep
    )

    assert desc_rep[0] in [1, 2]
    assert desc_rep[1] in [3, 4]
    assert desc_rep[2] in [5, 6]
