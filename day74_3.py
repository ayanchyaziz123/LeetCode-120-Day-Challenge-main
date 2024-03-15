class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        # Initialize variables to count uppercase and lowercase characters
        c = 0  # Count of uppercase characters
        s = 0  # Count of lowercase characters
        
        # Iterate through each character in the word
        for i in range(len(word)):
            # Check if the character is uppercase
            if word[i] >= 'A' and word[i] <= 'Z':
                c += 1  # Increment the count of uppercase characters
            else:
                s += 1  # Increment the count of lowercase characters
        
        # Check the conditions for capitalization rules
        if c > 0 and s > 0:  # If there are both uppercase and lowercase characters
            if word[0] >= 'A' and word[0] <= 'Z':  # If the first character is uppercase
                c -= 1  # Exclude the first character from the count of uppercase characters
                if c > 0 and s > 0:  # If there are still both uppercase and lowercase characters
                    return False  # Return False (capitalization rule violated)
            else:
                return False  # Return False (capitalization rule violated)
            
        # If the capitalization rules are satisfied, return True
        return True
