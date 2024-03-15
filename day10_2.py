import sys
from typing import List

class Solution:
    def solve(self, coins, amount, memo):
        # Base case: If the amount is 0, no coins needed.
        if amount == 0:
            return 0

        # If the result for the current amount is already memoized, return it.
        if memo[amount] != -1:
            return memo[amount]

        # Initialize the answer to the maximum integer value to find the minimum later.
        ans = sys.maxsize

        # Iterate through each coin denomination.
        for coin in coins:
            # If subtracting the current coin amount is a valid amount.
            if amount - coin >= 0:
                # Recursively calculate the minimum number of coins needed.
                ans = min(ans, self.solve(coins, amount - coin, memo) + 1)

        # Memoize the result for the current amount.
        memo[amount] = ans
        return ans

    def coinChange(self, coins: List[int], amount: int) -> int:
        # Initialize memoization array with -1 indicating that the result is not memoized.
        memo = [-1] * (amount + 1)

        # If the result is the maximum integer value, there is no valid combination.
        if self.solve(coins, amount, memo) == sys.maxsize:
            return -1

        # Return the minimum number of coins needed.
        return self.solve(coins, amount, memo)

# Time Complexity: O(N * M)
# N is the target amount, and M is the number of coin denominations.
# The memoization helps to avoid redundant calculations, making the algorithm more efficient.
# However, in the worst case, the algorithm explores all possible combinations of coins.
# Hence, the time complexity is proportional to the product of the target amount and the number of coin denominations.
