class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowelCount = 0  # Initialize the count of vowels
        vowels = ['a', 'e', 'i', 'o', 'u']  # List of vowel characters

        # Count vowels in the first k characters
        for i in range(k):
            if s[i] in vowels:
                vowelCount += 1

        mx = vowelCount  # Initialize the maximum vowel count

        # Iterate through the remaining characters in the string
        for i in range(k, len(s)):
            # Check if the current character is a vowel and update the count
            if s[i] in vowels:
                vowelCount += 1

            # Check if the character at position (i - k) is a vowel and update the count
            if s[i - k] in vowels:
                vowelCount -= 1

            # Update the maximum vowel count
            mx = max(mx, vowelCount)

        return mx  # Return the maximum vowel count
