from collections import defaultdict

class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        # Create a defaultdict to store the frequency of each number
        mp: dict = defaultdict(int)
        
        # Count the frequency of each number in the list
        for i in range(0, len(nums)):
            mp[nums[i]] += 1
        
        mx: int = -1  # Initialize the maximum frequency
        ans: int = 0  # Initialize the majority element
        
        # Iterate through the keys of the dictionary
        for key in mp:
            # Update the maximum frequency and majority element if a higher frequency is found
            if mp[key] > mx:
                mx = mp[key]
                ans = key
        
        return ans
