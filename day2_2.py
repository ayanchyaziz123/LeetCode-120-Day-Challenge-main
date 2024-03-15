class Solution:
    def rotate(self, matrix: list[list[int]]) -> None:
        # Transpose the matrix
        for i in range(0, len(matrix)):
            for j in range(i, len(matrix)):
                if i != j:
                    # Swap elements across the main diagonal
                    temp = matrix[i][j]
                    matrix[i][j] = matrix[j][i]
                    matrix[j][i] = temp

        # Reverse each row of the transposed matrix
        for i in range(0, len(matrix)):
            left = 0
            right = len(matrix[i]) - 1
            while left < right:
                # Swap elements in each row
                temp = matrix[i][left]
                matrix[i][left] = matrix[i][right]
                matrix[i][right] = temp
                left += 1
                right -= 1

# Example usage
matrix = [[5, 1, 9, 11],
          [2, 4, 8, 10],
          [13, 3, 6, 7],
          [15, 14, 12, 16]]

sl = Solution()
sl.rotate(matrix)

# Display the rotated matrix
for row in matrix:
    print(row)


      