class RecentCounter:

    def __init__(self):
        # Initialize a queue to store recent requests
        self.requests = []

    def ping(self, t: int) -> int:
        # Remove requests that fall outside the time frame [t - 3000, t]
        while self.requests and self.requests[0] < t - 3000:
            self.requests.pop(0)

        # Add the current request to the queue
        self.requests.append(t)

        # Return the number of requests in the time frame
        return len(self.requests)
