from typing import List

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        left = 0
        right = 0
        sum = 0
        mn = float('inf')  # Initialize mn to a large value
        
        while right < n:
            sum += nums[right]

            # Check if the current sum is greater than or equal to the target
            while sum >= target:
                # Update mn with the minimum length of the subarray
                mn = min(mn, right - left + 1)
                
                # Move the left pointer to shrink the subarray
                sum -= nums[left]
                left += 1

            # Move the right pointer to expand the subarray
            right += 1

        # Check if a valid subarray is found
        return mn if mn != float('inf') else 0
