class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        mx = 0  # Variable to store the maximum consecutive ones encountered
        res = 0  # Variable to store the current consecutive ones count
        for i in range(len(nums)):
            if nums[i] == 0:  # If the current number is 0
                res = 0  # Reset the consecutive ones count
            else:
                res += 1  # Increment the consecutive ones count
            mx = max(res, mx)  # Update the maximum consecutive ones count encountered
        return mx  # Return the maximum consecutive ones count
