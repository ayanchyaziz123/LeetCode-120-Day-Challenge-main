class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        # Initialize a count variable to track the number of right shifts
        count = 0
        
        # Continue right shifting both left and right until they are equal
        while left < right:
            left >>= 1  # Right shift left operand by 1
            right >>= 1  # Right shift right operand by 1
            count += 1  # Increment the count of right shifts
        
        # Left shift the final left value by the count to obtain the result
        return left << count
