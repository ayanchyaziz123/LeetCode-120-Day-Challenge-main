class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        # Iterate through each word in the list of words
        for word in words:
            l = 0  # Initialize the left pointer
            r = len(word) - 1  # Initialize the right pointer
            isValid = True  # Flag to indicate if the word is a palindrome
            
            # Loop to check if the word is a palindrome
            while l <= r:
                # If the characters at left and right pointers don't match, set isValid to False and break the loop
                if word[l] != word[r]:
                    isValid = False
                    break
                l += 1  # Move the left pointer towards the right
                r -= 1  # Move the right pointer towards the left
            
            # If the word is a palindrome, return it
            if isValid:
                return word
        
        # If no palindrome is found, return an empty string
        return ""
