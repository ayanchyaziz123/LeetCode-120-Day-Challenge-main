class Solution:
    def percentageLetter(self, s: str, letter: str) -> int:
        # Calculate the length of the input string
        n = len(s)
        
        # Initialize a counter for the occurrences of the specified letter
        cnt = 0
        
        # Iterate through each character in the input string
        for ch in s:
            # Check if the current character matches the specified letter
            if ch == letter:
                # If so, increment the counter
                cnt += 1
        
        # Calculate the percentage of occurrences of the specified letter in the string
        res = (cnt * 100) // n
        
        # Return the calculated percentage
        return res
