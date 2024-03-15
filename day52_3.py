from typing import List

class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        # Initialize empty strings to concatenate the words in both lists
        temp1 = ""
        
        # Iterate through words in the first list and concatenate them to temp1
        for word in word1:
            temp1 += word
        
        # Initialize another empty string to concatenate the words in the second list
        temp2 = ""
        
        # Iterate through words in the second list and concatenate them to temp2
        for word in word2:
            temp2 += word
        
        # Check if the concatenated strings from both lists are equal
        if temp1 == temp2:
            return True
        
        # If not equal, return False
        return False
