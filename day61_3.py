from typing import List

class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        # Calculate the length of the prefix
        n = len(pref)
        
        # Initialize a variable to store the count of words with the given prefix
        res = 0
        
        # Iterate over each word in the list of words
        for word in words:
            # Initialize a flag to track if the word starts with the given prefix
            flag = True
            
            # If the length of the word is less than the length of the prefix, skip it
            if len(word) < n:
                continue
            
            # Iterate over the characters in the prefix
            for i in range(n):
                # Check if the character in the word matches the corresponding character in the prefix
                if pref[i] != word[i]:
                    # If not, set the flag to False and break out of the loop
                    flag = False
                    break
            
            # If the flag is still True after checking all characters in the prefix,
            # it means the word starts with the given prefix, so increment the count
            if flag:
                res += 1
        
        # Return the count of words with the given prefix
        return res
