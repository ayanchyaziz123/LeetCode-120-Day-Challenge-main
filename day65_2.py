class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        # Calculate the minimum threshold for majority element occurrence
        n = len(nums) // 3
        
        # Dictionary to store frequency of each number
        mp = {}
        for val in nums:
            if val in mp:
                mp[val] += 1
            else:
                mp[val] = 1
        
        # List to store the majority elements
        res = []
        for key in mp:
            # If frequency of a number is greater than the threshold, add it to the result list
            if mp[key] > n:
                res.append(key)
        
        return res
