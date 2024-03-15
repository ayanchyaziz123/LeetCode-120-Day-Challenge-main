from typing import List

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        def bfs(row, col):
            # Initialize the queue with the starting point
            queue = [(row, col)]
            visited[row][col] = 1  # Mark as visited

            # Perform BFS
            while queue:
                r, c = queue.pop(0)
                for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    nr, nc = r + dr, c + dc
                    # Check if the neighbor is within the bounds, is 'O', and not visited
                    if 0 <= nr < m and 0 <= nc < n and board[nr][nc] == 'O' and not visited[nr][nc]:
                        queue.append((nr, nc))
                        visited[nr][nc] = 1  # Mark neighbor as visited

        if not board or not board[0]:
            return

        m, n = len(board), len(board[0])
        visited = [[0] * n for _ in range(m)]

        # Traverse the borders and perform BFS for 'O's on the borders
        for i in range(m):
            if board[i][0] == 'O' and not visited[i][0]:
                bfs(i, 0)
            if board[i][n-1] == 'O' and not visited[i][n-1]:
                bfs(i, n-1)

        for j in range(n):
            if board[0][j] == 'O' and not visited[0][j]:
                bfs(0, j)
            if board[m-1][j] == 'O' and not visited[m-1][j]:
                bfs(m-1, j)

        # Flip the surrounded 'O's to 'X' and revert '1's (visited) back to 'O'
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O' and not visited[i][j]:
                    board[i][j] = 'X'
                elif visited[i][j] == 1:
                    board[i][j] = 'O'

# Example usage:
board1 = [
    ["X", "X", "X", "X"],
    ["X", "O", "O", "X"],
    ["X", "X", "O", "X"],
    ["X", "O", "X", "X"]
]
solution = Solution()
solution.solve(board1)
print(board1)

board2 = [["X"]]
solution.solve(board2)
print(board2)
