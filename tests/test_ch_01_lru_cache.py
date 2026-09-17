import pytest
from ch_01_lru_cache import LRUCache

def test_standard_put_get():
    cache = LRUCache(2)
    cache.put(1, 100)
    cache.put(2, 200)
    assert cache.get(1) == 100
    assert cache.get(2) == 200

def test_standard_miss():
    cache = LRUCache(2)
    assert cache.get(999) == -1

@pytest.mark.edge_case
def test_edge_recency_refresh():
    cache = LRUCache(2)
    cache.put(1, 10)
    cache.put(2, 20)
    assert cache.get(1) == 10
    cache.put(3, 30)
    assert cache.get(2) == -1
    assert cache.get(1) == 10
    assert cache.get(3) == 30

@pytest.mark.edge_case
def test_edge_update_existing_capacity():
    cache = LRUCache(1)
    cache.put(5, 50)
    cache.put(5, 55)
    assert cache.get(5) == 55
