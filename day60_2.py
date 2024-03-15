from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        # Define a recursive function to solve the problem starting from 'start' index up to 'end' index
        def solve(start, end, dp):
            # If the solution for the current 'start' index is already computed, return it
            if dp[start] != -1:
                return dp[start]
            
            ans = 0  # Initialize the maximum amount that can be robbed
            
            # Loop through the houses starting from 'start' index up to 'end' index
            for i in range(start, end):
                # Decide whether to rob the current house or not
                # If robbing the current house, move to two houses ahead and add the current amount
                # If not robbing the current house, move to the next house and keep the current amount
                ans = max(ans, nums[i] + (solve(i + 2, end, dp) if i + 2 < end else 0))
                # Update the maximum amount that can be robbed starting from 'start' index
                dp[start] = ans
            
            return ans
        
        # Check for empty or single-house scenarios
        if not nums:
            return 0
        n = len(nums)
        if n == 1:
            return nums[0]
        
        # Initialize arrays to store the maximum amount that can be robbed with and without robbing the first house
        dp = [-1] * (n + 1)
        rob_first_house = solve(0, n - 1, dp)
        dp = [-1] * (n + 1)
        skip_first_house = solve(1, n, dp)
        
        # Return the maximum amount that can be robbed either by including or excluding the first house
        return max(rob_first_house, skip_first_house)
