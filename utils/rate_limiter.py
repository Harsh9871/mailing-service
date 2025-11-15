import time
from collections import defaultdict

class RateLimiter:
    def __init__(self, max_requests=5, window_ms=60000, trusted_ips=None):
        self.max_requests = max_requests
        self.window_ms = window_ms
        self.trusted_ips = set(trusted_ips) if trusted_ips else set()
        self.requests = defaultdict(list)
    
    def is_allowed(self, client_ip):
        # Skip rate limiting for trusted IPs and localhost
        if self._is_trusted_ip(client_ip):
            return True
        
        current_time = time.time() * 1000  # Convert to milliseconds
        window_start = current_time - self.window_ms
        
        # Clean old requests
        self.requests[client_ip] = [req_time for req_time in self.requests[client_ip] 
                                  if req_time > window_start]
        
        # Check if under limit
        if len(self.requests[client_ip]) < self.max_requests:
            self.requests[client_ip].append(current_time)
            return True
        
        return False
    
    def _is_trusted_ip(self, client_ip):
        localhost_ips = {'127.0.0.1', '::1', '::ffff:127.0.0.1'}
        return client_ip in localhost_ips or client_ip in self.trusted_ips