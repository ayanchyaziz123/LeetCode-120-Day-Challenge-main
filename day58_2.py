from collections import defaultdict
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Initialize a defaultdict to store anagrams
        res = defaultdict(list)
        
        # Iterate through each string in the input list
        for st in strs:
            # Initialize a temporary array to count the frequency of characters
            temp = [0] * 26
            
            # Count the frequency of each character in the current string
            for c in st:
                ind = ord(c) - ord('a')
                temp[ind] += 1
            
            # Convert the temporary array to a tuple to use it as a key in the defaultdict
            # Anagrams will have the same tuple key
            res[tuple(temp)].append(st)
        
        # Return a list containing lists of anagrams
        return res.values()
