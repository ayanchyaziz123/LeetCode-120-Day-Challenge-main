class Solution:
    def sumBase(self, n: int, k: int) -> int:
        res = 0  # Initialize the result variable to store the sum
        while 0 < n:  # Continue the loop until n becomes 0
            res += n % k  # Add the least significant digit (remainder of n divided by k) to the result
            n //= k  # Update n by integer dividing it by k, effectively removing the least significant digit
        return res  # Return the final sum
