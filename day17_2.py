from typing import List
class Solution:
    # XOR all elements in the array
    # 2 ^ 0 = 10 ^ 00 = 10
    # 1 ^ 2 = 01 ^ 10 = 11 
    # 2 ^ 3 = 10 ^ 11 = 01
    def singleNumber(self, nums: List[int]) -> int:
        number = 0
        for i in range(len(nums)):
            number ^= nums[i]
        return number   
nums = [2,1,2]
sol = Solution()
print(sol.singleNumber(nums))     


