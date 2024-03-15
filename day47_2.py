from typing import List
class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        sum_dig = 0
        row_size = len(mat)
        col_size = len(mat[0])
        r, c = 0, 0
        
        # Sum the elements in the main diagonal (top-left to bottom-right)
        while r < row_size and c < col_size:
            sum_dig += mat[r][c]
            r += 1
            c += 1
        
        r = 0
        c = col_size - 1
        
        # Sum the elements in the secondary diagonal (top-right to bottom-left)
        while r < row_size and c > -1:
            sum_dig += mat[r][c]
            r += 1
            c -= 1
        
        # If both row_size and col_size are odd, subtract the common element between diagonals
        if row_size % 2 != 0 and col_size % 2 != 0:
            mid_row = (row_size) // 2               
            mid_col = (col_size) // 2              
            sum_dig -= mat[mid_row][mid_col]
        
        return sum_dig
