from collections import Counter

class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        # Iterate through the elements of the list
        for i in range(len(nums)):
            # Count the frequency of each element using Counter
            freq = Counter(nums)
            
            # Initialize variables to store the maximum frequency and result
            mx = 0
            res = 0
            
            # Find the maximum frequency in the Counter dictionary
            for key in freq:
                if freq[key] > mx:
                    mx = freq[key]
            
            # Calculate the total count of elements with maximum frequency
            for key in freq:
                if freq[key] == mx:
                    res += mx
            
            # Return the total count of elements with maximum frequency
            return res
