from typing import List

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        # Initialize a memoization array to track occurrences of elements
        memo = [0] * 4001

        # Count occurrences of each element in the array
        for i in range(len(arr)):
            if arr[i] < 0:
                # Adjust index for negative numbers
                x = arr[i] + 3000
                memo[x] += 1
            else:
                memo[arr[i]] += 1

        # Check for unique occurrences
        temp = []
        for i in range(4001):
            # If occurrence count is already in temp, return False
            if memo[i] in temp and memo[i] != 0:
                return False
            temp.append(memo[i])

        # All occurrences are unique, return True
        return True
