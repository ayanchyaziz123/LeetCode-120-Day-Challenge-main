from typing import List

class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        def exploreGrid(r, c):
            # Initialize a queue for BFS
            queue = [(r, c)]
            # Mark the starting point as visited
            visited[r][c] = 1
            # Initialize flag, value, and count
            flag = True
            val = 1
            
            # Perform BFS
            while queue:
                curr_row, curr_col = queue.pop(0)
                
                # Explore neighbors in all directions
                for dx, dy in directions:
                    new_row, new_col = dx + curr_row, dy + curr_col
                    
                    # Check if the new position is within the grid
                    if new_row not in range(row_size) or new_col not in range(col_size):
                        flag = False
                    else:
                        # Check if the neighbor is unvisited and land
                        if grid[new_row][new_col] == 1 and not visited[new_row][new_col]:
                            queue.append((new_row, new_col))
                            visited[new_row][new_col] = 1
                            val += 1
            
            # Return the count if the entire component is within the grid, else return 0
            return val if flag else 0

        # Get the dimensions of the grid
        row_size = len(grid)
        col_size = len(grid[0])
        
        # Initialize a 2D array to track visited cells
        visited = [[0] * col_size for _ in range(row_size)]
        
        # Define directions for exploration: right, down, up, left
        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        
        # Initialize the count of enclaves
        cnt = 0

        # Iterate through each cell in the grid
        for r in range(row_size):
            for c in range(col_size):
                # Check if the cell is land and not visited
                if grid[r][c] == 1 and not visited[r][c]:
                    # Explore the connected component and update the count
                    val = exploreGrid(r, c)
                    cnt += val

        # Return the overall count of enclaves
        return cnt
