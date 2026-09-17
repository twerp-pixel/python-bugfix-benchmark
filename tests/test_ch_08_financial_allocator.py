import pytest
from ch_08_financial_allocator import allocate_shares

def test_standard_allocation():
    weights = {"AAPL": "0.50", "MSFT": "0.50"}
    res = allocate_shares("1000.00", weights)
    assert res == {"AAPL": "500.00", "MSFT": "500.00"}

@pytest.mark.edge_case
def test_edge_penny_rounding_invariant():
    weights = {"A": "0.3333", "B": "0.3333", "C": "0.3334"}
    res = allocate_shares("100.00", weights)
    total = sum(float(v) for v in res.values())
    assert abs(total - 100.00) < 1e-6
    assert res["C"] == "33.34"
