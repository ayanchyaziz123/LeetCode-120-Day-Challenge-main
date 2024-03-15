class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Set to store unique characters in the current substring
        charSet = set()
        
        # Length of the input string
        lenString = len(s)
        
        # Variable to track the maximum length of substring without repeating characters
        maxLen = 0
        
        # Variable to keep track of the left index of the current substring
        left = 0
        
        # Iterate through the characters of the string
        for i in range(lenString):
            # If the current character is not in the set, it's a unique character
            if s[i] not in charSet:
                charSet.add(s[i])
                
                # Update the maximum length if the current substring is longer
                maxLen = max(maxLen, ((i - left) + 1))
            else:
                # If the current character is already in the set, remove characters from the left
                # until the current character is no longer in the set
                while s[i] in charSet:
                    charSet.remove(s[left])
                    left += 1
                
                # Add the current character to the set
                charSet.add(s[i])
        
        # Return the maximum length of substring without repeating characters
        return maxLen

        
