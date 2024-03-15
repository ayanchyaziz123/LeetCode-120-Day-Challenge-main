from typing import List

class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        # Initialize a queue with the entrance coordinates and steps
        queue = [(entrance[0], entrance[1], 0)]
        # Define possible directions: up, down, left, right
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        m, n = len(maze), len(maze[0])
        # Set to keep track of visited cells
        visited = set()

        while queue:
            x, y, steps = queue.pop(0)

            # Skip if the cell is already visited or blocked by a wall
            if (x, y) in visited or maze[x][y] == '+':
                continue

            # Mark the cell as visited
            visited.add((x, y))

            # Check if the current cell is an exit and return the steps
            if (x, y) != (entrance[0], entrance[1]) and (x == 0 or x == m - 1 or y == 0 or y == n - 1):
                return steps

            # Explore neighbors in all directions
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                # Check if the neighbor is within the maze bounds, is an empty cell, and is not visited
                if 0 <= nx < m and 0 <= ny < n and maze[nx][ny] == '.' and (nx, ny) not in visited:
                    # Add the neighbor to the queue with updated steps
                    queue.append((nx, ny, steps + 1))

        # If no valid path is found, return -1
        return -1
