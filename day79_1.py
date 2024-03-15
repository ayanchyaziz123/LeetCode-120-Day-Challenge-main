class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        n = len(s)  # Get the length of the input string
        oneCnt = 0  # Initialize a counter for the number of '1's in the string
        for d in s:
            if d == '1':
                oneCnt += 1  # Count the number of '1's in the string
        
        oneCnt -= 1  # Decrement the counter by one to account for the '1' that will be added
        
        res = ""  # Initialize an empty string to store the result
        
        # Append '1's to the result string, excluding one '1' for the most significant bit
        for i in range(oneCnt):
            res += '1'
        
        # Append '0's to the result string to fill the remaining positions
        for i in range(n - oneCnt - 1):
            res += '0'
        
        # Append the final '1' to the result string as the most significant bit
        return res + '1'
