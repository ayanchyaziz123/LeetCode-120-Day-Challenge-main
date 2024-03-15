from typing import List

class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        # Sort the list of side lengths in descending order
        nums.sort(reverse=True)
        
        # Get the length of the list
        n = len(nums)
        
        # Initialize the maximum side length
        mx = nums[0]
        
        # Initialize the prefix sum of the remaining side lengths
        prfx_sum = 0
        
        # Calculate the prefix sum of the remaining side lengths
        for i in range(1, n):
            prfx_sum += nums[i]
        
        # Check if the prefix sum plus the maximum side length forms a valid polygon
        if prfx_sum > mx:
            return prfx_sum + mx
        
        # Iterate through the list to find the largest perimeter
        for j in range(1, n - 2):
            # Update the maximum side length and prefix sum
            mx = nums[j]
            prfx_sum -= nums[j]
            
            # Check if the current maximum side length plus the prefix sum forms a valid polygon
            if mx < prfx_sum:
                return mx + prfx_sum
        
        # If no valid polygon is found, return -1
        return -1
