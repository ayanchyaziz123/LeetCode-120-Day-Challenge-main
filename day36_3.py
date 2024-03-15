from typing import List

class Solution:
    def isGood(self, nums: List[int]) -> bool:
        # Create a list 'arr' to represent the expected sorted order of indices
        arr = []
        for i in range(len(nums) - 1):
            arr.append(i + 1)
        arr.append(len(nums) - 1)
        
        # Sort the input list 'nums'
        nums.sort()

        # Check if the sorted 'nums' list matches the expected 'arr' list
        if nums == arr:
            return True
        return False
