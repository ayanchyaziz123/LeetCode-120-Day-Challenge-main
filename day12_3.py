from typing import List

class Solution:
    def setRowNull(self, matrix, row):
        # Set all elements in the specified row to 0
        for i in range(len(matrix[0])):
            matrix[row][i] = 0

    def setColumnNull(self, matrix, column):
        # Set all elements in the specified column to 0
        for i in range(len(matrix)):
            matrix[i][column] = 0

    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Modify the input matrix in-place by setting rows and columns to zero based on zero entries.
        """
        # Arrays to mark which rows and columns have zero entries
        row = [False] * len(matrix)
        column = [False] * len(matrix[0])

        # Iterate through the matrix to find zero entries
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    # Mark the corresponding row and column
                    row[i] = True
                    column[j] = True

        # Iterate through the marked rows and set them to zero
        for i in range(len(row)):
            if row[i]:
                self.setRowNull(matrix, i)

        # Iterate through the marked columns and set them to zero
        for j in range(len(column)):
            if column[j]:
                self.setColumnNull(matrix, j)
