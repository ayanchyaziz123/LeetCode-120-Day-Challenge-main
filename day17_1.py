from typing import List
class Solution:
    # The time complexity is 0(n) 
    # n is the the size of array
    def missingNumber(self, nums: List[int]) -> int:
        # filling all the number 0 - n with 0
        # added one index beause one index value is missing
        hash = [0] * (len(nums) + 1)
        # if number is in array then filling hash index with 1
        for i in range(len(nums)):
            hash[nums[i]] = 1
        # if any index is empty then return the index
        for i in range(len(nums) + 1):
            if not hash[i]:
                return i
#nums = [9,6,4,2,3,5,7,0,1]
nums = [3,0,1]
sol = Solution()
print(sol.missingNumber(nums))           