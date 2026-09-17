import pytest
from ch_04_merge_intervals import merge_intervals

def test_standard_merge():
    intervals = [(1, 3), (2, 6), (8, 10), (15, 18)]
    expected = [(1, 6), (8, 10), (15, 18)]
    assert merge_intervals(intervals) == expected

@pytest.mark.edge_case
def test_edge_unsorted_input():
    intervals = [(8, 10), (1, 3), (15, 18), (2, 6)]
    expected = [(1, 6), (8, 10), (15, 18)]
    assert merge_intervals(intervals) == expected

@pytest.mark.edge_case
def test_edge_touching_boundaries():
    intervals = [(1, 4), (4, 5)]
    assert merge_intervals(intervals) == [(1, 5)]

@pytest.mark.edge_case
def test_edge_nested_intervals():
    intervals = [(1, 10), (2, 3), (4, 8)]
    assert merge_intervals(intervals) == [(1, 10)]
