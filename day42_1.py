from typing import List

class Solution:
    def subIslandExplore(self, grid1, grid2, r, c, row_size, col_size, visited):
        # Initialize a queue for BFS
        queue = []
        queue.append([r, c])
        
        # Define directions for exploring neighbors (right, down, left, up)
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        
        # Initialize a flag to determine if the current island is valid
        flag = True
        
        while queue:
            curr_row, curr_col = queue.pop(0)
            
            # Explore neighbors in all directions
            for dx, dy in directions:
                new_row = curr_row + dx
                new_col = curr_col + dy
                
                # Check if the new position is within the grid boundaries
                if new_row in range(row_size) and new_col in range(col_size):
                    if grid2[new_row][new_col] == 1 and not visited[new_row][new_col]:
                        # Check if the corresponding position in grid1 is 0
                        if grid1[new_row][new_col] == 0:
                            flag = False
                        # Add the new position to the queue and mark it as visited
                        queue.append([new_row, new_col])
                        visited[new_row][new_col] = 1
        
        # Return the flag indicating if the current island is valid
        return flag
            
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        row_size = len(grid1)
        col_size = len(grid1[0])
        
        # Initialize a 2D array to keep track of visited positions
        visited = [[0] * col_size for _ in range(row_size)]
        
        # Initialize a counter for the number of valid islands
        island_cnt = 0
        
        # Iterate through each position in the grids
        for r in range(row_size):
            for c in range(col_size):
                # Check if the position is part of an island in both grids and has not been visited
                    if grid1[r][c] == 1 and grid2[r][c] == 1 and not visited[r][c]:
                        if self.subIslandExplore(grid1, grid2, r, c, row_size, col_size, visited):
                           island_cnt += 1
        return island_cnt
