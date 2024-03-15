class Solution:
    def minimumLength(self, s: str) -> int:
        left, right = 0, len(s) - 1  # Initialize left pointer at start of string, right pointer at end of string
        
        # Continue until the pointers meet or cross
        while left < right and s[left] == s[right]:  # Check if characters at pointers are the same and pointers have not crossed
            c = s[left]  # Store the common character
            
            # Move left pointer to the right until a different character is encountered
            while left <= right and s[left] == c:
                left += 1
            
            # Move right pointer to the left until a different character is encountered
            while left <= right and s[right] == c:
                right -= 1
                
        return right - left + 1  # Calculate and return the length of the remaining substring
