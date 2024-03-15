from typing import List

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        memo = {}  # Dictionary to store computed results for dynamic programming

        def dp(i, curr_sum):
            # Base case: if all elements have been processed, return 1 if the current sum is zero, otherwise return 0
            if i == len(nums):
                return 1 if curr_sum == 0 else 0

            # If the current state has been computed before, return the value from the memoization table
            if (i, curr_sum) in memo:
                return memo[(i, curr_sum)]

            # Recursive calls for adding and subtracting the current number from the current sum
            # These represent taking the positive and negative paths respectively
            positive_count = dp(i + 1, curr_sum - nums[i])  # Subtract current number
            negative_count = dp(i + 1, curr_sum + nums[i])  # Add current number

            # Store the computed result in the memoization table
            memo[(i, curr_sum)] = positive_count + negative_count

            # Return the total count of ways to achieve the target sum
            return memo[(i, curr_sum)]

        # Start the dynamic programming recursion with the initial state of index 0 and target sum
        return dp(0, target)
