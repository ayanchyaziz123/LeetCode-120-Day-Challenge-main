class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        mx = 0  # Initialize a variable to store the maximum consecutive ones found
        res = 0  # Initialize a variable to store the current consecutive ones count
        
        # Iterate through the list
        for i in range(len(nums)):
            # If the current element is 0, reset the current consecutive ones count
            if nums[i] == 0:
                res = 0
            else:
                # If the current element is 1, increment the current consecutive ones count
                res += 1
                
            # Update the maximum consecutive ones count encountered so far
            mx = max(res, mx)
        
        # Return the maximum consecutive ones count
        return mx
