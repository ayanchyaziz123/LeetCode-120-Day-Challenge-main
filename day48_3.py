from typing import List

class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        def dfs(r, c, visited):
            if r < 0 or r >= row_size or c < 0 or c >= col_size or visited[r][c] or grid[r][c] == 0:
                return 0

            visited[r][c] = True
            current_gold = grid[r][c]

            # Explore all four directions
            down = dfs(r + 1, c, visited)
            right = dfs(r, c + 1, visited)
            up = dfs(r - 1, c, visited)
            left = dfs(r, c - 1, visited)

            visited[r][c] = False  # Backtrack

            # Return the maximum gold including the current cell
            return current_gold + max(down, right, up, left)

        row_size = len(grid)
        col_size = len(grid[0])
        max_gold = 0

        for r in range(row_size):
            for c in range(col_size):
                if grid[r][c] != 0:
                    # Perform DFS from each cell with gold
                    visited = [[False] * col_size for _ in range(row_size)]
                    max_gold = max(max_gold, dfs(r, c, visited))

        return max_gold

#
