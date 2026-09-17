import pytest
from ch_05_deep_dict_diff import deep_diff

def test_standard_diff():
    a = {"name": "Alice", "age": 30}
    b = {"name": "Alice", "age": 31, "city": "NYC"}
    diff = deep_diff(a, b)
    assert diff["added"] == {"city": "NYC"}
    assert diff["modified"]["age"] == {"old": 30, "new": 31}

@pytest.mark.edge_case
def test_edge_nested_type_mismatch():
    a = {"config": {"retries": 3}}
    b = {"config": "disabled"}
    diff = deep_diff(a, b)
    assert diff["modified"]["config"] == {"old": {"retries": 3}, "new": "disabled"}

@pytest.mark.edge_case
def test_edge_empty_dicts():
    assert deep_diff({}, {}) == {"added": {}, "removed": {}, "modified": {}}
