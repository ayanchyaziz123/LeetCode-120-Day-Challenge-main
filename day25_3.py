from typing import List
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        # Get the number of rows and columns in the image
        row_size = len(image)
        col_size = len(image[0])
        # Initialize a 2D array to keep track of visited cells
        visited = [[0] * col_size for _ in range(row_size)]
        # Initialize a queue for BFS traversal starting from the given pixel
        queue = []
        queue.append([sr, sc])
        # Get the original color of the starting pixel
        original_color = image[sr][sc]
        # Perform BFS traversal
        while queue:
            # Process the pixels at the current level
            for _ in range(len(queue)):
                r, c = queue.pop(0)
                # Update the color of the current pixel
                image[r][c] = color
                # Define directions: right, down, up, left
                directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
                # Explore neighbors in all directions
                for dx, dy in directions:
                    new_dx, new_dy = r + dx, c + dy
                    # Check if the new coordinates are within bounds
                    if 0 <= new_dx < row_size and 0 <= new_dy < col_size:
                        # Check if the neighboring pixel has the original color
                        if image[new_dx][new_dy] == original_color:
                            # Check if the pixel has not been visited
                            if not visited[new_dx][new_dy]:
                                # Add the neighboring pixel to the queue for further exploration
                                queue.append([new_dx, new_dy])

                                # Mark the pixel as visited
                                visited[new_dx][new_dy] = 1

        # Return the modified image after flood fill
        return image
