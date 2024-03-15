class Solution:
    def minimizedStringLength(self, s: str) -> int:
        res = set()  # Initialize an empty set to store unique characters
        for c in s:  # Iterate through each character in the string
            res.add(c)  # Add the character to the set (sets automatically handle duplicates)
        return len(res)  # Return the length of the set, which represents the number of unique characters
zsz