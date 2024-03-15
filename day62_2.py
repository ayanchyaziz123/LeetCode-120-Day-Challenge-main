from typing import List

class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        # Sort the input list of numbers
        nums.sort()
        
        # Dictionary to store results of subproblems
        memo = {}

        # Recursive function to find the largest divisible subset
        def dp(index, prev):
            # Base case: if all numbers are processed, return an empty list
            if index == len(nums):
                return []

            # If the result for this index and previous number is already computed, return it
            if (index, prev) in memo:
                return memo[(index, prev)]

            # Initialize empty lists to store subsets
            take = []

            # If the current number is divisible by the previous number, include it in the subset
            if nums[index] % prev == 0:
                take = [nums[index]] + dp(index + 1, nums[index])

            # Exclude the current number and move to the next index
            skip = dp(index + 1, prev)

            # Choose the subset with maximum length
            memo[(index, prev)] = max(take, skip, key=len)
            return memo[(index, prev)]

        # Start the recursion from the beginning of the list with previous number 1
        return dp(0, 1)

# Example usage:
solution = Solution()
nums1 = [1, 2, 3]
print(solution.largestDivisibleSubset(nums1))  # Output: [1, 2] or [1, 3]

nums2 = [1, 2, 4, 8]
print(solution.largestDivisibleSubset(nums2))  # Output: [1, 2, 4, 8]
