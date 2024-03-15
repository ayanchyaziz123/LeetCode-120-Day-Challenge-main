class Solution:
    def numSquares(self, n: int) -> int:
        # Generate perfect squares less than or equal to 'n'
        nums = []
        for i in range(1, n + 1):
            if i * i > n:  # If the square of the current number exceeds 'n', stop
                break
            nums.append(i*i)  # Append the square of the current number to the list of perfect squares
        print(nums)  # Print the list of perfect squares for debugging purposes
        
        # Define a recursive function to solve the problem
        def solve(n, memo):
            # Base cases
            if n == 0:  # If 'n' is 0, it's already represented as the sum of 0 perfect squares
                return 0
            if memo[n] != -1:  # If the result for 'n' is already computed, return it
                return memo[n]
            
            ans = float('inf')  # Initialize the result to positive infinity
            
            # Try all possible perfect squares less than or equal to 'n'
            for i in range(len(nums)):
                if n - nums[i] >= 0:  # If subtracting the current perfect square from 'n' results in a non-negative number
                    # Recursively solve for the remaining number after subtracting the perfect square,
                    # and add 1 to represent the current perfect square
                    ans = min(ans, solve(n-nums[i], memo) + 1)
                
                memo[n] = ans  # Memoize the result for 'n'
            
            return ans  # Return the result for 'n'
        
        # Initialize a memoization table to store computed results
        memo = [-1] * (n + 1)
        
        # Start the recursive function with the given 'n' and memoization table
        return solve(n, memo)  # Return the result computed by the recursive function
