class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        # Arrays to store mappings of characters
        mapping_s = [-1] * 256
        mapping_t = [-1] * 256

        for i in range(len(s)):
            char_s = ord(s[i]) - ord('a')
            char_t = ord(t[i]) - ord('a')

            # Check if the mapping is consistent for both s and t
            if mapping_s[char_s] == -1 and mapping_t[char_t] == -1:
                # If both mappings are not used, create a new mapping
                mapping_s[char_s] = char_t
                mapping_t[char_t] = char_s
            elif mapping_s[char_s] != char_t or mapping_t[char_t] != char_s:
                # If the mappings are inconsistent, strings are not isomorphic
                return False

        # If the loop completes, the strings are isomorphic
        return True
