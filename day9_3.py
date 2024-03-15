from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # Get the length of the input list
        n = len(digits)
        
        # Initialize a list to store the result
        ans = [0] * n
        
        # Initialize a variable to track the remainder from addition
        rem = 0
        
        # Iterate through the digits in reverse order
        for i in range(n - 1, -1, -1):
            # Check if it's the rightmost digit and needs carry
            if i == n - 1 and digits[i] + 1 == 10:
                rem = 1
                ans[i] = 0
            else:
                # Handle addition with the remainder
                if i == n - 1:
                    ans[i] = digits[i] + 1
                elif digits[i] + rem == 10:
                    ans[i] = 0
                    rem = 1
                else:
                    ans[i] = digits[i] + rem
                    rem = 0
        
        # If there's a remaining carry, add it to the front
        if rem:
            ans.insert(0, 1)
        
        # Return the final result
        return ans

# Time Complexity: O(n)
# The algorithm iterates through the digits once, where n is the length of the input list.
# Each iteration involves constant-time operations, resulting in a linear time complexity.
