from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # Counter to store the frequency of characters in t
        target_count = Counter(t)
        # Counter to keep track of characters in the current window
        window_count = Counter()

        # Function to check if all characters in t are present in the window
        def matches():
            for char, count in target_count.items():
                if window_count[char] < count:
                    return False
            return True

        # Initialize pointers and variables
        left, right = 0, 0
        min_length = float('inf')
        min_window = ""

        # Sliding window approach
        while right < len(s):
            # Expand the window from the right
            window_count[s[right]] += 1
            right += 1

            # Shrink the window from the left if it contains all characters in t
            while matches() and left < right:
                window_length = right - left
                if window_length < min_length:
                    min_length = window_length
                    min_window = s[left:right]
                
                # Shrink the window from the left
                window_count[s[left]] -= 1
                left += 1

        return min_window
