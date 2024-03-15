from typing import List

class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        # Get the length of the input list
        n = len(nums)
        
        # Initialize leftSum list to store cumulative sum of elements to the left of each index
        leftSum = [0] * n
        
        # Calculate cumulative sum from the left for each index
        for i in range(1, n):
            leftSum[i] += leftSum[i-1] + nums[i-1]
        
        # Initialize rightSum list to store cumulative sum of elements to the right of each index
        rightSum = [0] * n
        
        # Calculate cumulative sum from the right for each index
        for i in range(n-2, -1, -1):
            rightSum[i] += rightSum[i+1] + nums[i+1]
        
        # Initialize result list to store absolute differences between leftSum and rightSum for each index
        result = []
        
        # Calculate the absolute difference for each index and append to the result list
        for i in range(n):
            result.append(abs(leftSum[i] - rightSum[i]))
        
        # Return the final result list
        return result
