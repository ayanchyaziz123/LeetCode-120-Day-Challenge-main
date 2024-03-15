class Solution:
    def countPrefixes(self, words: List[str], s: str) -> int:
        cnt = 0  # Initialize the counter for matching prefixes
        
        # Iterate through each word in the list
        for word in words:
            # If the word is longer than the target string, skip it
            if len(word) > len(s):
                continue
            
            n = len(word)  # Length of the current word
            i = 0  # Index for iterating through characters of the word
            valid = True  # Flag to indicate if the prefix matches
            
            # Iterate through characters of the word and compare with characters of the target string
            while i < n:
                # If the characters don't match, set valid to False and break the loop
                if word[i] != s[i]:
                    valid = False
                    break
                i += 1  # Move to the next character
                
            # If the prefix is valid (matches), increment the counter
            if valid:
                cnt += 1
        
        # Return the total count of matching prefixes
        return cnt
