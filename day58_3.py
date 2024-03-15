from typing import List

class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        n = len(nums)
        
        # Sort the input array
        nums.sort()
        
        # If the length of the array is not divisible by 3, we cannot divide it into equal parts
        if n % 3 != 0:
            return []
        
        start = 0
        end = 3
        res = []
        
        # Iterate through the array in intervals of size 3
        while start < n:
            temp = []
            
            # Extract elements for the current interval
            while start < end:
                temp.append(nums[start])
                start += 1
            
            # Check if the difference between the maximum and minimum elements in the current interval is greater than k
            if temp[2] - temp[0] > k:
                return []
            
            # Append the current interval to the result
            res.append(temp)
            end += 3
        
        return res
