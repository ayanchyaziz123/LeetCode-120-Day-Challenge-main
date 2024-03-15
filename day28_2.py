class Solution:
    def firstUniqChar(self, s: str) -> int:
        # Initialize an array to store the count of each character in the alphabet
        char_count = [0] * 26
        # Count occurrences of each character in the input string
        for i in range(len(s)):
            char_index = ord(s[i]) - ord('a')
            char_count[char_index] += 1
        # Iterate through the string again to find the index of the first unique character
        for i in range(len(s)):
            char_index = ord(s[i]) - ord('a')
            # Check if the count of the character is 1 (indicating uniqueness)
            if char_count[char_index] == 1:
                return i
        # If no unique character is found, return -1
        return -1
