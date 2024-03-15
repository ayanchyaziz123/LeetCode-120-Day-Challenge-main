class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # Define a recursive helper function to solve the problem
        def solve(prev, curr):
            # Base case: if we've reached the end of the array, return 0
            if curr == len(nums):
                return 0
            
            # If the result for the current state is already calculated, return it
            if dp[prev + 1][curr] != -1:
                return dp[prev + 1][curr]
            
            taken = 0
            # If the current number is greater than the previous number, we can include it
            # Increment the length of the subsequence by 1 and move to the next number
            if prev == -1 or nums[prev] < nums[curr]:
                taken = solve(curr, curr + 1) + 1
            
            # Skip the current number and move to the next one
            skip = solve(prev, curr + 1)
            
            # Choose the maximum of including or excluding the current number
            ans = max(taken, skip)
            
            # Memoize the result for current state to avoid recomputation
            dp[prev + 1][curr] = ans
            return ans
        
        # Initialize a memoization table with -1 values
        dp = [[-1] * (len(nums) + 1) for _ in range(len(nums) + 1)]
        
        # Start the recursive process with prev=-1 and curr=0
        return solve(-1, 0)
