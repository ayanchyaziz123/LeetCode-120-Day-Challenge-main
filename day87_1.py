class Solution:
    def customSortString(self, order: str, s: str) -> str:
        # Count occurrences of each character in s
        char_count = {}
        for char in s:
            char_count[char] = char_count.get(char, 0) + 1
        
        # Build sorted string based on order
        sorted_string = ''
        for char in order:
            if char in char_count:
                sorted_string += char * char_count[char]
        
        # Append remaining characters not present in order
        for char in s:
            if char not in order:
                sorted_string += char
        
        return sorted_string
