from typing import List

class Solution:
    def bfs(self, land, r, c, row_size, col_size, visited):
        # Define possible directions: right, down, left, up
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        queue = []
        queue.append([r, c])
        # Initialize boundaries for the farmland
        min_row = r
        min_col = c
        max_row = r
        max_col = c
        while queue:
            queue_size = len(queue)
            # Process each element in the current level
            for _ in range(queue_size):
                curr_row, curr_col = queue.pop(0)
                for dx, dy in directions:
                    new_row = dx + curr_row
                    new_col = dy + curr_col
                    # Check if the new position is within the valid range
                    if new_row in range(row_size) and new_col in range(col_size):
                        # Check if the land at the new position is part of the farmland
                        if land[new_row][new_col] == 1:
                            if not visited[new_row][new_col]:
                                # Add the new position to the queue and update boundaries
                                queue.append([new_row, new_col])
                                visited[new_row][new_col] = 1
                                min_row = min(min_row, new_row)
                                min_col = min(min_col, new_col)
                                max_row = max(max_row, new_row)
                                max_col = max(max_col, new_col)
        return [min_row, min_col, max_row, max_col]

    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:
        row_size = len(land)
        col_size = len(land[0])
        visited = [[0] * col_size for _ in range(row_size)]
        result = []
        # Iterate through each cell in the land
        for i in range(row_size):
            for j in range(col_size):
                # Check if the cell is part of farmland and not visited
                if land[i][j] == 1 and not visited[i][j]:
                    # Perform BFS to find the boundaries of the farmland
                    temp = self.bfs(land, i, j, row_size, col_size, visited)
                    result.append(temp)
        return result
