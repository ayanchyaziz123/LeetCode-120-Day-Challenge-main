class Solution:
    def arrangeCoins(self, n: int) -> int:
        # Initialize result counter and row index
        res = 0
        row = 1

        # Continue until the remaining coins are positive
        while n > 0:
            # Check if the current row can be fully arranged with remaining coins
            if row <= n:
                res += 1

            # Deduct the coins used in the current row from the total
            n -= row
            
            # Move to the next row
            row += 1

        # Return the total number of complete rows arranged
        return res
