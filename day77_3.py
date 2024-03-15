class Solution:
    def largestOddNumber(self, num: str) -> str:
        n = len(num)
        
        # Check if the last digit is odd, if yes, return the number itself
        if int(num[n-1]) % 2 != 0:
            return num
        
        # Iterate through the digits of the number from right to left
        for i in range(n - 1, -1, -1):
            # Check if the digit is odd
            if int(num[i]) % 2 != 0:
                return num[:i+1]  # Return the substring from the beginning to the current index
        
        # If no odd digit is found, return an empty string
        return ""
