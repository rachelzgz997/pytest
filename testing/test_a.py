import pytest
@pytest.mark.parametrize('a', [1, 2, 3])
@pytest.mark.parametrize('b', [4, 5, 6])
def test_param(a, b):
    print(f"a = {a}, b = {b}")