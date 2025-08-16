from typing import List, Tuple

import pytest
from pytest_mock.plugin import MockerFixture

from evolvability.with_population.HGT.HGT_process_constant_genes_number import (
    HGTProcessConstantGenesNumber,
)


@pytest.fixture
def hgt_process_params() -> Tuple[Tuple[int, ...], int, List[Tuple[int, ...]], int]:
    """Fixture for common HGT process parameters."""
    rep = (0, 1, 0)
    length = 3
    population = [(1, 0, 1), (0, 0, 1), (0, 1, 1)]
    hgt_factor = 1
    return rep, length, population, hgt_factor


def test_no_HGT_process(
    hgt_process_params: Tuple[Tuple[int, ...], int, List[Tuple[int, ...]], int],
) -> None:
    """Tests that no HGT process occurs when HGT factor is zero."""
    rep, length, population, _ = hgt_process_params
    hgt_factor = 0
    hgt_process = HGTProcessConstantGenesNumber(hgt_factor, length, 1)

    mutated_rep = hgt_process.get_a_mutation_from_the_reps(rep, population)

    assert mutated_rep == rep


def test_HGT_process_occurred(
    hgt_process_params: Tuple[Tuple[int, ...], int, List[Tuple[int, ...]], int],
    mocker: MockerFixture,
) -> None:
    """Tests that HGT process correctly mutates a gene."""
    rep, length, population, hgt_factor = hgt_process_params
    hgt_process = HGTProcessConstantGenesNumber(hgt_factor, length, 1)
    gene_index = 2
    hgt_process.compute_percent_of_number_of_reps_in_population(population)

    mocker.patch.object(hgt_process, "get_random_gene_index", return_value=gene_index)

    mutated_rep = hgt_process.get_a_mutation_from_the_reps(rep, population)

    assert mutated_rep[gene_index] == 1


def test_compute_percent_of_number_of_reps_in_population(
    hgt_process_params: Tuple[Tuple[int, ...], int, List[Tuple[int, ...]], int],
) -> None:
    """Tests the computation of the percentage of reps with a gene."""
    rep, length, population, hgt_factor = hgt_process_params  # pylint: disable=W0612
    hgt_process = HGTProcessConstantGenesNumber(hgt_factor, length, 1)

    hgt_process.compute_percent_of_number_of_reps_in_population(population)

    assert hgt_process.fraction_of_reps_that_has_1 == [3**-1, 3**-1, 1]


def test_HGT_process_3_times(
    hgt_process_params: Tuple[Tuple[int, ...], int, List[Tuple[int, ...]], int],
    mocker: MockerFixture,
) -> None:
    """Tests the HGT process with a specific number of genes."""
    rep, length, population, hgt_factor = hgt_process_params
    number_of_genes = 3
    hgt_process = HGTProcessConstantGenesNumber(hgt_factor, length, number_of_genes)

    mocker.patch.object(hgt_process, "get_fraction_of_reps_with_gene", return_value=1)
    mutated_rep = hgt_process.get_a_mutation_from_the_reps(rep, population)
    assert mutated_rep == (1, 0, 1)
