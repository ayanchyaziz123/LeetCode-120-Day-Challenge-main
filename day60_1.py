from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        # Define a recursive function to solve the problem starting from 'start' index
        def solve(start, dp):
            # If the solution for the current 'start' index is already computed, return it
            if dp[start] != -1:
                return dp[start]
            
            ans = 0  # Initialize the maximum amount that can be robbed
            
            # Loop through the houses starting from 'start' index
            for i in range(start, len(nums)):
                # Decide whether to rob the current house or not
                # If robbing the current house, move to two houses ahead and add the current amount
                # If not robbing the current house, move to the next house and keep the current amount
                ans = max(ans, (solve(i+2, dp) + nums[i]))  # Update the maximum amount
                
                # Store the maximum amount that can be robbed starting from 'start' index
                dp[start] = ans
            
            return ans
        
        # Initialize an array to store the maximum amount that can be robbed starting from each index
        dp = [-1] * (len(nums) + 10)  # Adding extra space for safety
        
        # Start solving the problem from the beginning (0th index) and return the result
        return solve(0, dp)
