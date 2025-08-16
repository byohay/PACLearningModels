from typing import List

import pytest
from pytest_mock.plugin import MockerFixture

from PAC.PAC_Algorithm import PAC_Algorithm


@pytest.fixture
def pac_algorithm(mocker: MockerFixture) -> PAC_Algorithm:
    """Fixture for PAC_Algorithm with a mocked oracle."""
    oracle = mocker.Mock()
    return PAC_Algorithm(oracle, 4)


def test_get_current_hypo(pac_algorithm: PAC_Algorithm) -> None:
    """Tests that get_current_hypo raises ValueError when no hypothesis is set."""
    with pytest.raises(ValueError):
        pac_algorithm.get_current_hypo()


def test_eliminate_unfit_from_current_hypo(pac_algorithm: PAC_Algorithm) -> None:
    """Tests the elimination of unfit hypotheses from the current hypothesis."""
    sample: List[int] = [1, -1, 1, 1]

    pac_algorithm.eliminate_unfit_from_current_hypo(sample)
    assert pac_algorithm.get_current_hypo() == [1, -1, 1, 1]

    sample2: List[int] = [1, -1, -1, 1]

    pac_algorithm.eliminate_unfit_from_current_hypo(sample2)
    assert pac_algorithm.get_current_hypo() == [1, -1, 0, 1]
