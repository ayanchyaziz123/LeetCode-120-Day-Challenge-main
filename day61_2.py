class Solution:
    def tribonacci(self, n: int) -> int:
        # Dictionary to store computed results for memoization
        memo = {}
        
        # Recursive function to calculate the nth Tribonacci number
        def solve(n, memo):
            # Base cases
            if n < 0:
                return 0
            if n == 1 or n == 2:
                return 1
            
            # If the result for the current 'n' is already computed, return it from memoization
            if n in memo:
                return memo[n]
            
            # Compute the Tribonacci number recursively and store the result in memoization
            memo[n] = solve(n-1, memo) + solve(n-2, memo) + solve(n-3, memo)
            return memo[n]
        
        # Start the recursion from n and return the result
        return solve(n, memo)
