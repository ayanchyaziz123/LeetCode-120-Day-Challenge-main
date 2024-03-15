from typing import List

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        row_size = len(grid)
        col_size = len(grid[0])
        visited = [[0] * col_size for _ in range(row_size)]

        def solve(r, c, memo):
            # Check for invalid cases and return a large value
            if r not in range(row_size) or c not in range(col_size) or visited[r][c]:
                return float('inf')
            
            # Check if we reached the destination
            if r == (row_size - 1) and c == (col_size - 1):
                return grid[r][c]

            # Check if the result for the current cell is already computed
            if memo[r][c] != -1:
                return memo[r][c]
            
            visited[r][c] = 1

            # Move right and down, choose the minimum path
            right_path = solve(r, c + 1, memo)
            down_path = solve(r + 1, c, memo)
            
            visited[r][c] = 0

            # Store the computed result in the memoization table
            memo[r][c] = grid[r][c] + min(right_path, down_path)
            
            return memo[r][c]

        # Initialize the memoization table with -1
        memo = [[-1] * col_size for _ in range(row_size)]
        
        # Start the recursion with memoization
        return solve(0, 0, memo)

# Example usage:
# solution = Solution()
# grid = [[1,3,1],[1,5,1],[4,2,1]]
# result = solution.minPathSum(grid)
# print(result)
