from typing import List
class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        def explore(board, r, c, visited, row_size, col_size):
            # Base case checks
            if r not in range(row_size) or c not in range(col_size):
                return
            if visited[r][c]:
                return
            if board[r][c] == "X":
                visited[r][c] = 1
                # Explore adjacent cells
                explore(board, r + 1, c, visited, row_size, col_size)
                explore(board, r, c + 1, visited, row_size, col_size)

        row_size = len(board)
        col_size = len(board[0])
        visited = [[0] * col_size for _ in range(row_size)]
        cnt_val = 0

        # Iterate through the board cells
        for r in range(row_size):
            for c in range(col_size):
                if board[r][c] == "X" and not visited[r][c]:
                    # If an unvisited "X" cell is found, increment count and explore connected cells
                    cnt_val += 1
                    explore(board, r, c, visited, row_size, col_size)

        return cnt_val

