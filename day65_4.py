class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        # Initialize a list to store the frequency of each character
        hash = [0] * 26
        
        # Count the frequency of each character in the string
        for c in s:
            ind = ord(c) - ord('a')  # Get the index of the character in the hash list
            hash[ind] += 1
        
        val = 0  # Initialize a variable to store the frequency of the first character
        i = 0  # Initialize an index variable to iterate through the hash list
        
        # Find the frequency of the first non-zero character in the hash list
        while val == 0 and i < 26:
            val = hash[i]
            i += 1
        
        # Iterate through the hash list to check if all frequencies are equal to val
        for h in hash:
            if h != 0 and val != h:
                return False
        
        # If all frequencies are equal to val, return True
        return True
