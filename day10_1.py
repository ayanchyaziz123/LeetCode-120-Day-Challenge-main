class Solution:
    def solve(self, n: int, memo: list):
        # Base case: if n is negative, there is no way to climb
        if n < 0:
            return 0
        # Base case: if n is 0, there is one way (no steps needed)
        elif n == 0:
            return 1
        # Check if the result for n has already been calculated
        elif memo[n] > -1:
            return memo[n]
        # Recursively calculate the number of ways to climb for n
        else:
            memo[n] = self.solve(n - 1, memo) + self.solve(n - 2, memo)
            return memo[n]

    def climbStairs(self, n: int) -> int:
        # Initialize a list to store computed results
        memo = [-1] * (n+1)
        # Start the recursive solving process
        return self.solve(n, memo)