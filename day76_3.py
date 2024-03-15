from typing import List

class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        # Create a dictionary to store the frequency of each element
        freq = {}
        
        # Count the frequency of each element in the array
        for num in arr:
            if num not in freq:
                freq[num] = 1
            else:
                freq[num] += 1
        
        # Iterate over the dictionary keys
        for key in freq:
            # Check if the frequency of the element is 1 (distinct)
            if freq[key] == 1:
                k -= 1  # Decrement k since we found a distinct element
            # If k becomes 0, return the current element
            if k == 0:
                return key
        
        # If kth distinct element is not found, return an empty string
        return ""
