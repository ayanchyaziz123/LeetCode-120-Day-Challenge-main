class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        # Initialize variables to store the index of the dominant number and its value
        ind = -1  # Index of the dominant number
        mx = -1   # Value of the dominant number
        
        # Find the dominant number (the largest number) and its index in the list
        for i in range(len(nums)):
            if mx < nums[i]:
                mx = nums[i]
                ind = i
        
        # Sort the list of numbers in ascending order
        nums.sort()
        
        # Check if the largest number is at least twice as large as every other number
        n = len(nums) - 1  # Index of the largest number in the sorted list
        for i in range(len(nums) - 1):
            if nums[n] < (nums[i] * 2):
                return -1  # If the condition is not satisfied, return -1
        
        # Return the index of the dominant number
        return ind
