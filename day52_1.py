from typing import List

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # Get the size of the board
        row_size = len(board)
        col_size = len(board[0])
        
        # Initialize a 2D array to keep track of visited cells
        visited = [[0] * col_size for _ in range(row_size)]
        
        # Define a recursive function for DFS
        def dfs(r, c, ind):
            # Base case: If all characters in the word are matched, return True
            if ind == len(word):
                return True
            
            # Check for out-of-bounds, visited, and mismatch conditions
            if r not in range(row_size) or c not in range(col_size) or visited[r][c] or board[r][c] != word[ind]:
                return False
            
            # Mark the current cell as visited
            visited[r][c] = 1
            
            # Recursively explore adjacent cells in all directions
            result = dfs(r+1, c, ind+1) or dfs(r, c+1, ind+1) or dfs(r-1, c, ind+1) or dfs(r, c-1, ind+1)
            
            # Backtrack by marking the current cell as not visited
            visited[r][c] = 0
            
            # Return the result of the exploration
            return result
        
        # Iterate through all cells in the board to start DFS
        for r in range(row_size):
            for c in range(col_size):
                # If DFS starting from this cell returns True, the word exists in the board
                if dfs(r, c, 0):
                    return True
        
        # If no match is found after exploring all cells, return False
        return False
