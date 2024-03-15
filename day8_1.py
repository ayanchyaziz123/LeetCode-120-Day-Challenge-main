class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # Start from the end of the string
        i = len(s) - 1
        
        # Skip trailing spaces
        while s[i] == ' ' and 0 <= i:
            i -= 1
        
        # Initialize a counter 
        #for the length of the last word
        cnt = 0
        
        # Count the characters of the last word
        while s[i] != ' ' and 0 <= i:
            i -= 1
            cnt += 1
        
        # If there are no words, count the characters 
        #until the beginning of the string
        if cnt == 0:
            while 0 <= i:
                cnt += 1
        
        return cnt
