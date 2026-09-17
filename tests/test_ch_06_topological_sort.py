import pytest
from ch_06_topological_sort import topological_sort, CycleDetectedError

def test_standard_dag():
    graph = {
        "app": ["db", "redis"],
        "db": ["os"],
        "redis": ["os"],
        "os": []
    }
    order = topological_sort(graph)
    assert order.index("os") < order.index("db")
    assert order.index("os") < order.index("redis")
    assert order.index("db") < order.index("app")
    assert order.index("redis") < order.index("app")

@pytest.mark.edge_case
def test_edge_cycle_detection():
    graph = {
        "A": ["B"],
        "B": ["C"],
        "C": ["A"]
    }
    with pytest.raises(CycleDetectedError):
        topological_sort(graph)

@pytest.mark.edge_case
def test_edge_disconnected_nodes():
    graph = {"A": [], "B": [], "C": []}
    order = topological_sort(graph)
    assert set(order) == {"A", "B", "C"}
