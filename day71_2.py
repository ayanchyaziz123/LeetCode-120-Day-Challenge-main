class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        # Check if n is 0, as 0 is not a power of 2
        if n == 0:
            return False
        
        # While n is not 1, continue looping
        while n != 1:
            # If n is not divisible by 2, it cannot be a power of 2
            if n % 2 != 0:
                return False
            
            # Divide n by 2 to check if it is a power of 2
            n = n // 2
        
        # If the loop exits with n being 1, it is a power of 2
        return True
