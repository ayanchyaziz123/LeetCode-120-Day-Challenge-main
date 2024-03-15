class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        # Find the index of the character 'ch' in the word
        i = 0
        while i < len(word) and word[i] != ch:
            i += 1
        
        res = ""
        # If the character 'ch' is not found, return the original word
        if i == len(word):
            return word
        
        # Reverse the substring from the beginning up to the index of 'ch'
        x = i + 1
        while i != -1:
            res += word[i]
            i -= 1
        
        # Append the remaining characters after 'ch'
        while x < len(word):
            res += word[x]
            x += 1
        
        return res
