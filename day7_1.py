from typing import List
#Leetcode problem:-> 15. 3Sum
#Ayan's code
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []
        nums.sort()  # Sort the array to simplify the solution

        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i-1]:
                continue  # Skip duplicate values for the first element of the triplet

            left, right = i + 1, len(nums) - 1

            while left < right:
                total = nums[i] + nums[left] + nums[right]

                if total < 0:
                    left += 1
                elif total > 0:
                    right -= 1
                else:
                    ans.append([nums[i], nums[left], nums[right]])

                    # Skip duplicate values for the second and third elements of the triplet
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1

                    left += 1
                    right -= 1

        return ans

# Example usage:
solution = Solution()
nums = [-1, 0, 1, 2, -1, -4]
result = solution.threeSum(nums)
print(result)
