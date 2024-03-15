from typing import List

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        # Create a hash list to count occurrences of each number
        hash = [0] * (len(nums) + 1)
        
        # Iterate through the input nums and update hash counts
        for i in range(len(nums)):
            hash[nums[i]] += 1
        
        # Initialize an empty list to store missing numbers
        ans = []    
        
        # Iterate through the hash list from 1 to len(hash) - 1
        for i in range(1, len(hash)):
            # If the count for a number is 0, it means the number is missing
            if hash[i] == 0:
                # Add the missing number to the ans list
                ans.append(i)
        
        # Return the list of disappeared numbers
        return ans
