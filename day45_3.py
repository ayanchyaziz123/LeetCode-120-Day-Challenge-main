from typing import List

class Solution:
    def catchFish(self, grid, r, c, row_size, col_size, visited):
        # Initialize a queue for BFS
        queue = [(r, c)]
        # Mark the starting point as visited
        visited[r][c] = 1
        # Initialize total catch
        total_catch = 0
        # Define directions for exploration: right, down, up, left
        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        
        # Perform BFS to catch fish
        while queue:
            curr_row, curr_col = queue.pop(0)
            # Accumulate the catch at the current position
            total_catch += grid[curr_row][curr_col]
            
            # Explore neighbors in all directions
            for dx, dy in directions:
                new_row, new_col = dx + curr_row, dy + curr_col
                
                # Check if the new position is within the grid
                if new_row not in range(row_size) or new_col not in range(col_size):
                    continue
                
                # Check if the neighbor has fish and is not visited
                if grid[new_row][new_col] > 0 and not visited[new_row][new_col]:
                    queue.append((new_row, new_col))
                    visited[new_row][new_col] = 1
        
        # Return the total catch from the BFS
        return total_catch

    def findMaxFish(self, grid: List[List[int]]) -> int:
        row_size = len(grid)
        col_size = len(grid[0])
        # Initialize a 2D array to track visited cells
        visited = [[0] * col_size for _ in range(row_size)]
        # Initialize the maximum total catch
        max_total = 0
        
        # Iterate through each cell in the grid
        for r in range(row_size):
            for c in range(col_size):
                # Check if the cell has fish and is not visited
                if grid[r][c] > 0 and not visited[r][c]:
                    # Update the maximum total catch
                    max_total = max(max_total, self.catchFish(grid, r, c, row_size, col_size, visited))
        
        # Return the overall maximum total catch
        return max_total
