class BrowserHistory:

    def __init__(self, homepage: str):
        # Initialize the BrowserHistory with a list containing the homepage
        self.history = [homepage]
        # Initialize pointers: current points to the current page, max_index is the maximum index in the history
        self.current = 0
        self.max_index = 0

    def visit(self, url: str) -> None:
        # When visiting a new URL, clear forward history
        self.history = self.history[:self.current + 1]
        # Append the new URL to the history list
        self.history.append(url)
        # Update pointers
        self.current += 1
        self.max_index = self.current

    def back(self, steps: int) -> str:
        # Move back in history, but ensure the minimum index is 0
        self.current = max(0, self.current - steps)
        # Return the current URL after moving back
        return self.history[self.current]

    def forward(self, steps: int) -> str:
        # Move forward in history, but ensure not to exceed the maximum index
        self.current = min(self.max_index, self.current + steps)
        # Return the current URL after moving forward
        return self.history[self.current]

# Example usage:
browserHistory = BrowserHistory("leetcode.com")
browserHistory.visit("google.com")
browserHistory.visit("facebook.com")
browserHistory.visit("youtube.com")
print(browserHistory.back(1))      # Output: "facebook.com"
print(browserHistory.back(1))      # Output: "google.com"
print(browserHistory.forward(1))   # Output: "facebook.com"
browserHistory.visit("linkedin.com")
print(browserHistory.forward(2))   # Output: "linkedin.com" (cannot move forward)
print(browserHistory.back(2))      # Output: "google.com"
print(browserHistory.back(7))      # Output: "leetcode.com"
