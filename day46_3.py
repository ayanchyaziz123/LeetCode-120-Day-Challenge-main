class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        i = 0
        ans = ""

        # Iterate through the characters in the input string
        while 0 < k and i < len(s):
            # Check if the current character is a space
            if s[i] == ' ':
                k -= 1

                # Check if we have reached the desired number of words (k == 0)
                if k == 0:
                    return ans

            # Add the current character to the result string
            ans += s[i]
            i += 1

        # Return the truncated sentence
        return ans
