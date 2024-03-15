class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        # Sort the input array
        nums.sort()
        
        # Initialize variables
        i = 0  # Index for iterating through the sorted array
        res = 0  # Variable to store the sum of pairs
        
        # Get the length of the array
        n = len(nums)
        
        # Iterate through the sorted array
        while i < n:
            # Add the element at even index to the result
            if i % 2 == 0:
                res += nums[i]
            i += 2  # Move to the next even index
            
        # Return the sum of pairs
        return res
