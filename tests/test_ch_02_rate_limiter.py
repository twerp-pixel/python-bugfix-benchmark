import pytest
from ch_02_rate_limiter import SlidingWindowRateLimiter

def test_standard_limit():
    limiter = SlidingWindowRateLimiter(max_requests=2, window_seconds=10.0)
    assert limiter.allow_request(1.0) is True
    assert limiter.allow_request(2.0) is True
    assert limiter.allow_request(3.0) is False

@pytest.mark.edge_case
def test_edge_window_expiry():
    limiter = SlidingWindowRateLimiter(max_requests=2, window_seconds=5.0)
    assert limiter.allow_request(1.0) is True
    assert limiter.allow_request(2.0) is True
    assert limiter.allow_request(6.1) is True

@pytest.mark.edge_case
def test_edge_exact_boundary_collision():
    limiter = SlidingWindowRateLimiter(max_requests=1, window_seconds=2.0)
    assert limiter.allow_request(1.0) is True
    assert limiter.allow_request(3.0) is True
