class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        hash = [0] * 1001  # Initialize a hash table to count occurrences of positive numbers
        nums.sort()  # Sort the input list of numbers
        
        mx = -1001  # Initialize a variable to track the maximum k
        
        # Count occurrences of positive numbers
        for i in range(len(nums)):
            if nums[i] >= 0:
                hash[nums[i]] += 1
        
        # Iterate through the sorted list of numbers
        for i in range(len(nums)):
            if nums[i] <= 0:  # Check for negative numbers
                x = abs(nums[i])  # Get the absolute value of the negative number
                if hash[x] > 0 and mx < nums[i]:  # If the absolute value exists in the hash table and is greater than the current maximum k
                    mx = x  # Update the maximum k
        
        if mx == -1001:  # If no positive number was found
            return -1  # Return -1
        
        return mx  # Return the maximum k
