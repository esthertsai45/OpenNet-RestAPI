import pytest


def find_missing_number(input: list) -> int:
    if not all(isinstance(x, int) for x in input):
        raise ValueError("Input must be a list of integers")

    sorted_input = sorted(input)
    for i in range(len(sorted_input)):
        if sorted_input[i] != i:
            return i
    return 0


@pytest.mark.parametrize(
    "input, expected", [
        ([3, 0, 1], 2),
        ([0, 1], 0),
        ([9, 6, 4, 2, 3, 5, 7, 0, 1], 8),
        ([0, 2, 3, 4, 5, 6, 7, 8, 9], 1),
        ([0, 1, 3, 4, 5, 6, 7, 8, 9], 2)
    ]
)
def test_missing_number(input: list, expected: int):
    assert find_missing_number(input) == expected
