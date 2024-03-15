from typing import List
#Leetcode problem:-> 167. Two Sum II - Input Array Is Sorted
#Ayan's code
# Time Complexity: 0(n)
# As the item is sorted, so no need to sort the array.
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1
        while left < right:
            sm = numbers[left] + numbers[right]
            # if sum == target 
            if sm == target:  
                return [left+1, right+1]
            # if  target value is bigger
            elif sm < target: 
                left += 1
            # if sum value is not bigger than target    
            else: 
                right -= 1 
        return []         
        