from typing import List

from conjunction import Conjunction


def test_is_function_answering_yes_on_sample__answer_no() -> None:
    """Tests if is_function_answering_yes_on_sample correctly returns False."""
    conjunction = Conjunction(6)
    function: List[int] = [1, 1, -1, 0, -1, 0]

    x: List[int] = [1, 1, 1, 1, -1, 1]

    assert not conjunction.is_function_answering_yes_on_sample(x, function)


def test_is_function_answering_yes_on_sample__answer_yes() -> None:
    """Tests if is_function_answering_yes_on_sample correctly returns True."""
    conjunction = Conjunction(6)
    function: List[int] = [1, 1, -1, 0, -1, 0]

    x: List[int] = [1, 1, -1, 1, -1, 1]

    assert conjunction.is_function_answering_yes_on_sample(x, function)


def test_get_random_false_sample() -> None:
    """Tests if get_random_false_sample generates a sample that returns False."""
    conjunction = Conjunction(6)
    for i in range(10000):
        function: List[int] = [1, 1, -1, 0, -1, 0]
        conjunction.ideal_function = function

        sample: List[int] = conjunction.get_random_false_sample()

        assert not conjunction.is_function_answering_yes_on_sample(sample, function)
