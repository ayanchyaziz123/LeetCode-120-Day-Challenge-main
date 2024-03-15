from typing import List

class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def is_valid(row, col, num):
            # Check if the number can be placed in the current row, column, and subgrid
            for i in range(9):
                # checking all entire row, col and 3*3 grid
                if board[row][i] == num or board[i][col] == num or board[3 * (row // 3) + i // 3][3 * (col // 3) + i % 3] == num:
                    return False
            return True

        def solve():
            for i in range(9):
                for j in range(9):
                    if board[i][j] == '.':
                        for num in map(str, range(1, 10)):
                            if is_valid(i, j, num):
                                board[i][j] = num
                                if solve():
                                    return True
                                board[i][j] = '.'  # Backtrack if the current placement is invalid
                        return False
            return True

        solve()