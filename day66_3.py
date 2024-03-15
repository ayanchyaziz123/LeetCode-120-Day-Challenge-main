import collections  # Import the collections module to use Counter

class Solution:
    def equalFrequency(self, word: str) -> bool:
        # Iterate through each character position in the word
        for i in range(len(word)):
            # Remove the character at index i from the word
            newWord = word[:i] + word[i + 1:]
            
            # Count the frequency of each character in the modified word
            freq = collections.Counter(newWord)
            
            # Check if the maximum frequency is equal to the minimum frequency
            if max(freq.values()) == min(freq.values()):
                return True  # If the frequencies are equal, return True
        
        return False  # If no such character found, return False
