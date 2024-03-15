from typing import List

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        def solve(start, amount, dp):
            # Base case: if amount becomes 0, return 1
            if amount == 0:
                return 1
            if dp[start][amount] != -1:
                return dp[start][amount]
            # Initialize the result for this level
            result = 0

            # Iterate through the coins starting from the current index
            for i in range(start, len(coins)):
                # Check if the current coin value is less than or equal to the remaining amount
                if amount - coins[i] >= 0:
                    # Recursively call the function with updated start index and remaining amount
                    result += solve(i, amount - coins[i], dp)

            # Update the memoization table after the loop
            dp[start][amount] = result

            # Return the result for this level
            return result

        # Initialize the answer variable
        ans = 0
        dp = [[-1] * (amount + 1) for _ in range(len(coins) + 1)]
        # Call the recursive function with the starting index as 0 and the given amount
        ans = solve(0, amount, dp)
        # Return the final answer
        return ans
