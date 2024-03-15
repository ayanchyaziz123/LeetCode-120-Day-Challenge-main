class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)  # Length of the input string
        count = 0  # Initialize the count of palindromic substrings
        
        # Helper function to expand around center
        def expand_around_center(left, right):
            nonlocal count  # Access the count variable from the outer function
            # Expand outwards from the center as long as characters match
            while left >= 0 and right < n and s[left] == s[right]:
                count += 1  # Increment count for each palindromic substring found
                left -= 1  # Move left pointer towards left
                right += 1  # Move right pointer towards right
        
        # Loop to handle odd length palindromes
        for i in range(n):
            expand_around_center(i, i)  # Call helper function with the same center
        
        # Loop to handle even length palindromes
        for i in range(n - 1):
            expand_around_center(i, i + 1)  # Call helper function with adjacent centers
        
        return count  # Return the total count of palindromic substrings

# Example usage:
sol = Solution()
s1 = "abc"
print(sol.countSubstrings(s1))  # Output: 3

s2 = "aaa"
print(sol.countSubstrings(s2))  # Output: 6
