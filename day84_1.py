class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        # Get the number of rows and columns in the grid
        row_size = len(grid)
        col_size = len(grid[0])
        
        # Initialize the result counter
        res = 0
        
        # Iterate over each row and column in reverse order
        for r in range(row_size):
            for c in range(col_size-1, -1, -1):
                # Check if the current element is negative
                if grid[r][c] < 0:
                    res += 1  # If negative, increment the result counter
                else:
                    break  # If non-negative, break out of the loop as all further elements will be non-negative
        
        # Return the count of negative numbers
        return res
