from typing import List

class Solution:
    def matrixSum(self, nums: List[List[int]]) -> int:
        # Sort each row in the matrix in ascending order
        for r in range(len(nums)):
            nums[r].sort()

        # Initialize a variable to store the total sum of maximum values in each column
        score = 0    

        # Iterate over columns in reverse order
        for c in range(len(nums[0])-1, -1, -1):
            # Initialize a variable to track the maximum value in the current column
            mx = float('-inf')

            # Iterate over rows in reverse order to find the maximum value in the current column
            for r in range(len(nums)-1, -1, -1):
                mx = max(mx, nums[r][c])

            # Add the maximum value in the current column to the total score
            score += mx

        # Return the final total score
        return score
