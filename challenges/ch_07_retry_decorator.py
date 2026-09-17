"""Challenge 07: Exponential Backoff Retry Decorator."""
import functools

def retry(max_attempts=3, delay=0.01, exceptions=(Exception,)):
    def decorator(func):
        # BUG: Missing @functools.wraps erases function metadata
        def wrapper(*args, **kwargs):
            # BUG: Off-by-one attempt counter retries fewer times than max_attempts
            attempts = 0
            while attempts < max_attempts - 1:
                try:
                    return func(*args, **kwargs)
                except exceptions:
                    attempts += 1
            # BUG: Unconditional call bypasses exception filter
            return func(*args, **kwargs)
        return wrapper
    return decorator
