class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        def dfs(r, c, visited, dp):
            # Check if we reached the destination
            if r == (m-1) and c == (n-1):
                return 1
            
            # Check if the current cell is out of bounds or already visited
            if r not in range(m) or c not in range(n) or visited[r][c]:
                return 0
            
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

        # Initialize the visited array and dp array with appropriate dimensions
        visited = [[0] * n for _ in range(m)]
        dp = [[-1] * n for _ in range(m)]
        
        # Start DFS from the top-left corner
        return dfs(0, 0, visited, dp)
