from typing import List

class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        # Sort the input list
        nums.sort()
        
        # Get the length of the list
        n = len(nums)
        
        # Initialize the result variable
        res = 0
        
        # Iterate through all pairs of numbers in the sorted list
        for i in range(n):
            for j in range(i + 1, n):
                # Check if the sum of the current pair is less than the target
                if nums[i] + nums[j] < target:
                    # If so, increment the result count
                    res += 1
        
        # Return the final count of pairs whose sum is less than the target
        return res
