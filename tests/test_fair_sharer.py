# test for fair_sharer.py

import pytest
from src.fair_sharer import fair_sharer

def test_fair_sharer_one_iteration():
    assert fair_sharer([0, 1000, 800, 0], 1) == [100, 800, 900, 0], "Test case for one iteration failed"

def test_fair_sharer_multiple_iterations():
    assert fair_sharer([0, 1000, 800, 0], 5) == [268.29, 634.3199999999999, 726.49, 170.9], "Test case for multiple iterations failed"
