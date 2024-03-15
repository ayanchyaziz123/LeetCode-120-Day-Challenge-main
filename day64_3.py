class Solution:
    def isPrefixOfWord(self, sentence: str, s: str) -> int:
        # Split the sentence into individual words
        words = sentence.split()
        
        # Iterate through each word in the list
        for i in range(len(words)):
            # If the length of the current word is shorter than the prefix, skip it
            if len(words[i]) < len(s):
                continue
            
            n = len(s)  # Length of the prefix
            j = 0  # Initialize the index for iterating through characters of the prefix
            valid = True  # Flag to indicate if the prefix matches
            
            # Iterate through characters of the prefix and compare with characters of the current word
            while j < n:
                # If the characters don't match, set valid to False and break the loop
                if words[i][j] != s[j]:
                    valid = False
                    break
                j += 1  # Move to the next character
                
            # If the prefix is valid (matches), return the index of the word
            if valid:
                return i + 1  # Add 1 to convert from 0-based index to 1-based index
        
        # If no word with the prefix is found, return -1
        return -1
