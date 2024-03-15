from typing import List

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        def solve(i, n, memo):
            # Base case: If already reached or beyond the last step, cost is 0
            if i >= n:
                return 0
            
            # If the result for this index is already computed, return it
            if memo[i]:
                return memo[i]
            
            # Compute the minimum cost for the current step and store it in memo
            memo[i] = cost[i] + min(solve(i+1, n, memo), solve(i+2, n, memo))
            
            # Return the computed cost for the current step
            return memo[i]

        # Initialize memoization array with zeros
        memo = [0] * len(cost)
        
        # Return the minimum cost starting from both the 0th and 1st step
        return min(solve(0, len(cost), memo), solve(1, len(cost), memo))
