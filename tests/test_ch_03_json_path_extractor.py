import pytest
from ch_03_json_path_extractor import extract_json_path

def test_standard_dict_lookup():
    data = {"user": {"profile": {"name": "Alice"}}}
    assert extract_json_path(data, "user.profile.name") == "Alice"
    assert extract_json_path(data, "user.missing", "DEF") == "DEF"

@pytest.mark.edge_case
def test_edge_falsy_preservation():
    data = {"stats": {"count": 0, "active": False, "tag": ""}}
    assert extract_json_path(data, "stats.count", -1) == 0
    assert extract_json_path(data, "stats.active", True) is False
    assert extract_json_path(data, "stats.tag", "fallback") == ""

@pytest.mark.edge_case
def test_edge_list_indexing():
    data = {"users": [{"id": 10}, {"id": 20}]}
    assert extract_json_path(data, "users.1.id") == 20
    assert extract_json_path(data, "users.99.id", default=None) is None
