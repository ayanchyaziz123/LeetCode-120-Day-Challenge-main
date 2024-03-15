from typing import List

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [0] * n  # Initialize result array
        
        left, right = 0, n - 1  # Pointers for the leftmost and rightmost elements of nums
        
        # Iterate over the nums array from the end towards the beginning
        for i in range(n - 1, -1, -1):
            # Compare the absolute values of the leftmost and rightmost elements
            if abs(nums[left]) > abs(nums[right]):
                result[i] = nums[left] * nums[left]  # Square the leftmost element
                left += 1  # Move left pointer to the right
            else:
                result[i] = nums[right] * nums[right]  # Square the rightmost element
                right -= 1  # Move right pointer to the left
        
        return result
