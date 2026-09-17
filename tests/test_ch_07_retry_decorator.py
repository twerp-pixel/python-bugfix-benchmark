import pytest
from ch_07_retry_decorator import retry

def test_standard_retry_success():
    calls = 0
    @retry(max_attempts=3, delay=0.0)
    def flaky():
        nonlocal calls
        calls += 1
        if calls < 2:
            raise ValueError("Temporary failure")
        return "success"
    
    assert flaky() == "success"
    assert calls == 2

@pytest.mark.edge_case
def test_edge_unhandled_exception_raises_immediately():
    calls = 0
    @retry(max_attempts=5, delay=0.0, exceptions=(KeyError,))
    def raises_type_error():
        nonlocal calls
        calls += 1
        raise TypeError("Fatal error")
        
    with pytest.raises(TypeError):
        raises_type_error()
    assert calls == 1

@pytest.mark.edge_case
def test_edge_wraps_metadata_preserved():
    @retry(max_attempts=2, delay=0.0)
    def sample_func():
        """My docstring."""
        return 42
    assert sample_func.__name__ == "sample_func"
    assert sample_func.__doc__ == "My docstring."
