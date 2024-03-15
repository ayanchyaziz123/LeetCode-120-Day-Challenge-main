class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        # Initialize a hash table to count occurrences of each number
        hash = [0] * (len(nums) + 1)
        
        # Iterate through the numbers and count their occurrences
        for i in range(len(nums)):
            hash[nums[i]] += 1
        
        # Initialize a variable to store the duplicate number
        res = 0
        
        # Iterate through the numbers again to find the duplicate
        for i in range(len(nums)):
            if hash[nums[i]] == 2:
                res = nums[i]
        
        # Iterate through the hash table to find the missing number
        for i in range(1, len(hash) + 1):
            if hash[i] == 0:
                # Return the duplicate and missing numbers as a list
                return res, i
