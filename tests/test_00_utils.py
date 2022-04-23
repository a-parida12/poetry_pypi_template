import pytest

from hapy_pypi import bool_val

@pytest.mark.base
def test_00_1_base_test():
    assert type(bool_val) == bool
    assert bool_val == True

