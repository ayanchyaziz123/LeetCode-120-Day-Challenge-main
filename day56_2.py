from typing import List

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        def dfs(r, c, visited, dp):
            # Check if the current cell is out of bounds, already visited, or contains an obstacle
            if r not in range(row_size) or c not in range(col_size) or visited[r][c] or obstacleGrid[r][c] == 1:
                return 0
            
            # Check if we reached the destination
            if r == (row_size - 1) and c == (col_size - 1):
                return 1
            
            # Check if the result for the current cell is already computed
            if dp[r][c] != -1:
                return dp[r][c]
            
            ans = 0
            visited[r][c] = 1
            
            # Explore right and down directions
            ans += dfs(r+1, c, visited, dp) + dfs(r, c+1, visited, dp)
            
            visited[r][c] = 0
            
            # Store the computed result in the dp array
            dp[r][c] = ans
            
            return ans

        # Get the dimensions of the obstacleGrid
        row_size = len(obstacleGrid)
        col_size = len(obstacleGrid[0])
        
        # Initialize the visited array and dp array with appropriate dimensions
        visited = [[0] * col_size for _ in range(row_size)]
        dp = [[-1] * col_size for _ in range(row_size)]
        
        # Start DFS from the top-left corner
        return dfs(0, 0, visited, dp)
