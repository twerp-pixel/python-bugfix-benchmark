"""Challenge 02: Sliding Window Rate Limiter."""

class SlidingWindowRateLimiter:
    def __init__(self, max_requests: int, window_seconds: float):
        self.max_requests = max_requests
        self.window_seconds = window_seconds
        self.requests = []

    def allow_request(self, current_time: float) -> bool:
        # BUG: Off-by-one comparison and strictly greater check drops valid requests
        cutoff = current_time - self.window_seconds
        self.requests = [t for t in self.requests if t > cutoff]
        if len(self.requests) > self.max_requests:  # BUG: strictly greater allows max+1 requests!
            return False
        self.requests.append(current_time)
        return True
