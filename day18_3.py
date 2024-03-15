from typing import List

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        # Initialize an empty list to store the output (duplicates)
        output = []
        
        # Iterate through the input nums
        for i in range(len(nums)):
            # Calculate the index to access in the nums list
            ind = abs(nums[i]) - 1
            
            # Check if the value at the calculated index is already negative
            if nums[ind] < 0:
                # If it is negative, it means the number has been seen before, and it is a duplicate
                # Append the absolute value of the current number (ind + 1) to the output list
                output.append(ind + 1)
            
            # Mark the number at the calculated index as seen by making it negative
            nums[ind] = -nums[ind]
        
        # Return the list of duplicates
        return output
