from typing import List

class Solution:
    def exploreIsland(self, grid, r, c, row_size, col_size, visited):
        queue = []
        queue.append([r, c])
        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        flag = True
        while queue:
            curr_row, curr_col = queue.pop(0)
            for dx, dy in directions:
                new_row = dx + curr_row
                new_col = dy + curr_col
                # Check if the new position is within the grid boundaries
                if new_row not in range(row_size) or new_col not in range(col_size):
                    flag = False
                else:
                    # If the cell is land (0) and not visited, add to the queue and mark as visited
                    if grid[new_row][new_col] == 0 and not visited[new_row][new_col]:
                        queue.append([new_row, new_col])
                        visited[new_row][new_col] = 1
        return flag

    def closedIsland(self, grid: List[List[int]]) -> int:
        row_size = len(grid)
        col_size = len(grid[0])
        visited = [[0] * col_size for i in range(row_size)]
        cnt = 0
        for r in range(row_size):
            for c in range(col_size):
                # If the cell is land (0) and not visited, explore the island and increment the count
                if grid[r][c] == 0 and not visited[r][c]:
                    if self.exploreIsland(grid, r, c, row_size, col_size, visited):
                        cnt += 1
        return cnt
