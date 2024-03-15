from typing import List

class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        # Separate odd and even numbers into separate lists
        odd = []
        even = []
        for i in range(len(nums)):
            if nums[i] % 2 == 0:  # If the number is even
                even.append(nums[i])  # Add it to the even list
            else:  # If the number is odd
                odd.append(nums[i])  # Add it to the odd list
        
        n = len(nums)  # Get the length of the input list
        j = 0  # Initialize the index for even numbers
        k = 0  # Initialize the index for odd numbers
        res = []  # Initialize the result list
        i = 0  # Initialize the index for traversing through the input list

        # Traverse through the input list
        while i < n:
            if i % 2 == 0:  # If the index is even
                res.append(even[j])  # Append the next even number
                j += 1  # Move to the next even number
            else:  # If the index is odd
                res.append(odd[k])  # Append the next odd number
                k += 1  # Move to the next odd number
            i += 1  # Move to the next index

        return res  # Return the sorted list
