from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        
        def solve(nums, current_permutation):
            # Base case: if nums is empty, the current_permutation is a valid permutation
            if not nums:
                result.append(current_permutation[:])  # Append a copy of the current_permutation
                return
            
            # Iterate through each element in nums
            for i in range(len(nums)):
                val = nums[i]
                current_permutation.append(val)  # Include the current element in the permutation
                solve(nums[:i] + nums[i+1:], current_permutation)  # Recursively solve for the remaining elements
                current_permutation.pop()  # Backtrack: remove the last element to explore other possibilities
            
        solve(nums, [])  # Start the recursion with an empty current_permutation
        return result

# Example usage:
solution = Solution()
nums = [1, 2, 3]
result = solution.permute(nums)
print(result)
