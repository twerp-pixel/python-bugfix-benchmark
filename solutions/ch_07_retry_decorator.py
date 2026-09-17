"""Reference Solution: Exponential Backoff Retry Decorator."""
import functools
import time

def retry(max_attempts=3, delay=0.01, exceptions=(Exception,)):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            last_err = None
            for attempt in range(1, max_attempts + 1):
                try:
                    return func(*args, **kwargs)
                except exceptions as e:
                    last_err = e
                    if attempt < max_attempts and delay > 0:
                        time.sleep(delay)
            raise last_err
        return wrapper
    return decorator
