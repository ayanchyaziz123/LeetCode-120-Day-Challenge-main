from typing import List

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()  # Sort the input list to handle duplicates
        
        def solve(nums, current_permutation):
            if not nums:
                result.append(current_permutation[:])  # Append a copy of the current_permutation
                return
            
            for i in range(len(nums)):
                # Skip duplicates by checking if the current element is the same as the previous one
                if i > 0 and nums[i] == nums[i - 1]:
                    continue
                
                val = nums[i]
                current_permutation.append(val)
                solve(nums[:i] + nums[i+1:], current_permutation)
                current_permutation.pop()  # Backtrack
            
        solve(nums, [])
        return result

# Example usage:
solution = Solution()
nums = [1, 1, 2]
result = solution.permuteUnique(nums)
print(result)
