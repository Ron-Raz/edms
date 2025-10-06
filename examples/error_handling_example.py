"""Simple exponential backoff helper for transient API errors."""
import time, random

def with_backoff(fn, retries=5, base=0.5, cap=10.0):
    """Retry a function call with exponential backoff and jitter."""
    for i in range(retries):
        try:
            return fn()
        except Exception as e:
            if i == retries - 1:
                raise
            sleep = min(cap, base * (2 ** i)) + random.uniform(0, 0.25)
            print(f"Retrying after {sleep:.2f}s due to: {e}")
            time.sleep(sleep)

# Example usage
if __name__ == "__main__":
    def flaky():
        """A placeholder function that sometimes fails."""
        import requests
        return requests.get("https://httpstat.us/200", timeout=5).status_code

    print(with_backoff(flaky))
