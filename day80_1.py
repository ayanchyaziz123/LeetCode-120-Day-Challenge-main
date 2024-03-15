class Solution:
    def checkAlmostEquivalent(self, word1: str, word2: str) -> bool:
        # Initialize frequency lists for both words, each with 26 slots for each lowercase letter
        freq1 = [0] * 26
        freq2 = [0] * 26
        
        # Get the length of the words (assuming both words are of equal length)
        n = len(word1)
        
        # Iterate through each character of the words
        for i in range(n):
            # Get the index of the current character in word1 and word2
            ind1 = ord(word1[i]) - ord('a')  # Convert character to its corresponding index in the frequency list
            ind2 = ord(word2[i]) - ord('a')
            
            # Increment the frequency count for the respective character in both words
            freq1[ind1] += 1
            freq2[ind2] += 1
        
        # Initialize a counter for the difference between frequencies of characters
        cnt = 0
        
        # Iterate through each character (letter) in the alphabet
        for i in range(26):
            # If the absolute difference between frequencies of a character in both words is greater than 3
            if abs(freq1[i] - freq2[i]) > 3:
                # Return False, as the words are not "almost equivalent"
                return False
        
        # If the loop completes without returning False, return True, indicating the words are "almost equivalent"
        return True
