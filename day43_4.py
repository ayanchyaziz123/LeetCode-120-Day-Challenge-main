from typing import List

class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        result = []
        
        # Iterate through each element in nums
        for i in range(len(nums)):
            val = -1
            j = i + 1
            flag = False
            
            # Check the elements to the right of the current element
            while j < len(nums):
                if nums[i] < nums[j]:
                    val = nums[j]
                    flag = True
                    break
                j += 1
            
            # If no greater element to the right, check the elements to the left (circular)
            if not flag:
                k = 0
                while k < i:
                    if nums[i] < nums[k]:
                        val = nums[k]
                        break
                    k += 1
            
            # Append the result for the current element
            result.append(val)
        
        return result

# Example usage:
solution = Solution()
nums = [1, 2, 1]
result = solution.nextGreaterElements(nums)
print(result)
