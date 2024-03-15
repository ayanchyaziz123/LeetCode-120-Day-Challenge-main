from typing import List

class Solution:
    def distinctDifferenceArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = []

        for i in range(n):
            # Count the number of distinct elements in the prefix nums[0, ..., i]
            distinct_prefix = len(set(nums[:i+1]))

            # Count the number of distinct elements in the suffix nums[i + 1, ..., n - 1]
            distinct_suffix = len(set(nums[i+1:]))

            # Calculate the distinct difference and append to the result list
            diff = distinct_prefix - distinct_suffix
            result.append(diff)

        return result

# Example usage
nums = [1, 2, 3, 4, 5]
sol = Solution()
output = sol.distinctDifferenceArray(nums)
print(output)