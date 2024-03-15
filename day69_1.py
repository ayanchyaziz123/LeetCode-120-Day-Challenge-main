import heapq

class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        # Get the number of rows and columns in the heights grid
        rows, cols = len(heights), len(heights[0])
        
        # Define the directions: right, down, left, up
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        
        # Initialize the priority queue with the top-left cell (row, col, effort)
        pq = [(0, 0, 0)]
        
        # Initialize efforts matrix with infinity
        efforts = [[float('inf')] * cols for _ in range(rows)]
        efforts[0][0] = 0
        
        # Iterate while the priority queue is not empty
        while pq:
            # Pop the node with the minimum effort from the priority queue
            effort, row, col = heapq.heappop(pq)
            
            # If we reach the bottom-right cell, return its effort
            if row == rows - 1 and col == cols - 1:
                return effort
            
            # Explore neighboring cells
            for dr, dc in directions:
                new_row, new_col = row + dr, col + dc
                
                # Check if the neighboring cell is within the grid boundaries
                if 0 <= new_row < rows and 0 <= new_col < cols:
                    # Calculate the effort to reach the neighboring cell
                    new_effort = max(effort, abs(heights[new_row][new_col] - heights[row][col]))
                    
                    # If the new effort is less than the current effort of the neighboring cell, update it
                    if new_effort < efforts[new_row][new_col]:
                        efforts[new_row][new_col] = new_effort
                        heapq.heappush(pq, (new_effort, new_row, new_col))
        
        # If the bottom-right cell is not reached, return -1
        return -1
