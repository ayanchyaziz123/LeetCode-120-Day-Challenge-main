from typing import List

class Solution:
    def getVisitedArray(self, n, m):
        """
        Create a 2D array for visited nodes initialized to 0.

        Parameters:
        - n: Number of rows
        - m: Number of columns

        Returns:
        - vis: 2D array initialized to 0
        """
        vis = []
        for i in range(n):
            temp = []
            for j in range(m):
                temp.append(0)
            vis.append(temp)
        return vis

    def bfs(self, grid, vis, i, j, n, m):
        """
        Perform Breadth-First Search (BFS) traversal from the given node.

        Parameters:
        - grid: The grid of '1's and '0's
        - vis: 2D array indicating visited nodes
        - i: Row index of the starting node
        - j: Column index of the starting node
        - n: Number of rows in the grid
        - m: Number of columns in the grid
        """
        queue = []
        queue.append([i, j])
        while queue:
            current = queue.pop(0)  # Change variable name to 'current'
            x = current[0]
            y = current[1]
            direction = [[1, 0], [-1, 0], [0, 1], [0, -1]]
            for dirx, diry in direction:
                a = dirx + x
                b = diry + y
                if 0 <= a <= n and 0 <= b <= m and grid[a][b] == "1" and vis[a][b] == 0:
                    queue.append([a, b])
                    vis[a][b] = 1

    def numIslands(self, grid: List[List[str]]) -> int:
        """
        Count the number of islands in the grid.

        Parameters:
        - grid: The grid of '1's and '0's

        Returns:
        - ans: The number of islands
        """
        n = len(grid)
        m = len(grid[0])
        vis = self.getVisitedArray(n, m)
        ans = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == "1" and vis[i][j] == 0:
                    ans += 1
                    self.bfs(grid, vis, i, j, n-1, m-1)
        return ans
