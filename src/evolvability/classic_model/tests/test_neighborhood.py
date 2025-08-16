from typing import Set, Tuple

import pytest

from evolvability.classic_model.monotone_conjunction_algorithm.conjunction_neighborhood import (
    MonotoneConjunctionNeighborhood,
)


@pytest.fixture
def neighbors_finder() -> MonotoneConjunctionNeighborhood:
    """Fixture for MonotoneConjunctionNeighborhood."""
    return MonotoneConjunctionNeighborhood()


def test_find_for_zero(neighbors_finder: MonotoneConjunctionNeighborhood) -> None:
    """Tests finding the neighborhood for a zero representation."""
    neighbors: Set[Tuple[int, ...]] = set()
    neighbors.add((0, 0, 0, 0, 0))
    neighbors.add((1, 0, 0, 0, 0))
    neighbors.add((0, 1, 0, 0, 0))
    neighbors.add((0, 0, 1, 0, 0))
    neighbors.add((0, 0, 0, 1, 0))
    neighbors.add((0, 0, 0, 0, 1))

    assert neighbors == neighbors_finder.get_neighborhood_of_rep((0, 0, 0, 0, 0))


def test_find_for_other(neighbors_finder: MonotoneConjunctionNeighborhood) -> None:
    """Tests finding the neighborhood for a non-zero representation."""
    neighbors: Set[Tuple[int, ...]] = set()

    neighbors.add((0, 0, 0, 0, 0))

    neighbors.add((1, 0, 0, 0, 0))
    neighbors.add((0, 1, 0, 0, 0))
    neighbors.add((0, 0, 1, 0, 0))
    neighbors.add((0, 0, 0, 1, 0))
    neighbors.add((0, 0, 0, 0, 1))

    neighbors.add((1, 0, 1, 0, 0))
    neighbors.add((0, 1, 1, 0, 0))
    neighbors.add((0, 0, 1, 1, 0))
    neighbors.add((0, 0, 1, 0, 1))

    assert neighbors == neighbors_finder.get_neighborhood_of_rep((0, 0, 1, 0, 0))


def test_find_for_another_one(neighbors_finder: MonotoneConjunctionNeighborhood) -> None:
    """Tests finding the neighborhood for another non-zero representation."""
    neighbors: Set[Tuple[int, ...]] = set()

    neighbors.add((1, 1, 1, 1, 0))

    neighbors.add((1, 1, 1, 0, 1))
    neighbors.add((1, 1, 0, 1, 1))
    neighbors.add((1, 0, 1, 1, 1))
    neighbors.add((0, 1, 1, 1, 1))

    neighbors.add((1, 1, 1, 0, 0))
    neighbors.add((1, 1, 0, 1, 0))
    neighbors.add((1, 0, 1, 1, 0))
    neighbors.add((0, 1, 1, 1, 0))
    neighbors.add((1, 1, 1, 1, 1))

    assert neighbors == neighbors_finder.get_neighborhood_of_rep((1, 1, 1, 1, 0))


def test_find_for_unique(neighbors_finder: MonotoneConjunctionNeighborhood) -> None:
    """Tests finding the neighborhood for a unique two-element representation."""
    neighbors: Set[Tuple[int, ...]] = set()

    neighbors.add((1, 0))
    neighbors.add((0, 1))
    neighbors.add((0, 0))
    neighbors.add((1, 1))

    assert neighbors == neighbors_finder.get_neighborhood_of_rep((0, 1))
