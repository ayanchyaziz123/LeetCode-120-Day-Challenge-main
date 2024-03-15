class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        # Initialize a list to store the frequency of each character
        hash = [0] * 26
        
        # Count the frequency of each character in the sentence
        for c in sentence:
            ind = ord(c) - ord('a')  # Get the index of the character in the hash list
            hash[ind] += 1
        
        # Iterate through the hash list to check if any character has a frequency of 0
        for h in hash:
            if h == 0:
                return False  # If any character is missing, return False
        
        # If all characters are present (i.e., frequencies are non-zero), return True
        return True
