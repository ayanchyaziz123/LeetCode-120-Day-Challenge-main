class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        memo = {}  # Dictionary to store computed results
        
        # Recursive function to perform DFS and find maximum cherries
        def dfs(r, c1, c2):
            # If already computed, return the memoized result
            if (r, c1, c2) in memo:
                return memo[(r, c1, c2)]
            
            # Base cases:
            # If out of bounds or same column for both robots, return 0 cherries
            if r < 0 or r >= row_size or c1 < 0 or c1 >= col_size or c2 < 0 or c2 >= col_size or c1 == c2:
                return 0
            
            # If at the last row, return cherries at the current cells
            if r == row_size - 1:
                return grid[r][c1] + grid[r][c2]
            
            res = 0  # Initialize maximum cherries
            
            # Explore all possible movements for both robots
            for c1_d in [-1, 0, 1]:
                for c2_d in [-1, 0, 1]:
                    # Update the maximum cherries by considering the next row
                    res = max(res, dfs(r + 1, c1 + c1_d, c2 + c2_d))
            
            # Store the result in the memo dictionary and return
            memo[(r, c1, c2)] = res + grid[r][c1] + (grid[r][c2] if c1 != c2 else 0)
            return memo[(r, c1, c2)]

        # Get the number of rows and columns in the grid
        row_size = len(grid)
        col_size = len(grid[0])
        
        # Start DFS from the top row with robots at the given columns
        return dfs(0, 0, col_size - 1)
