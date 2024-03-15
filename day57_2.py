class Solution:
    def longestPalindrome(self, s: str) -> int:
        # Initialize an array to store the count of each character
        hash = [0] * 60

        # Count the occurrences of each character in the input string
        for i in range(len(s)):
            ind = ord(s[i]) - ord('A')
            hash[ind] += 1

        # Initialize the result counter and a flag to check if there is an odd count
        res = 0
        isOdd = False

        # Iterate through the character count array
        for i in range(len(hash)):
            if hash[i] > 0:
                # If the count is even, add it directly to the result
                if hash[i] % 2 == 0:
                    res += hash[i]
                else:
                    # If the count is odd, add (count - 1) to the result
                    isOdd = True
                    res += (hash[i] - 1)

        # If there is at least one character with an odd count, add 1 to the result
        if isOdd:
            return res + 1

        # If all characters have even counts, return the result as is
        return res
