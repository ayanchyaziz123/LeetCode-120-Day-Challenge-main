class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        # Get the number of rows and columns in the original matrix
        rows = len(matrix)
        cols = len(matrix[0])
        
        # Create a new matrix with dimensions swapped
        transposed_matrix = [[0] * rows for _ in range(cols)]
        
        # Traverse through each element of the original matrix
        for i in range(rows):
            for j in range(cols):
                # Place the element at matrix[i][j] in the transposed_matrix[j][i]
                transposed_matrix[j][i] = matrix[i][j]
        
        # Return the transposed matrix
        return transposed_matrix
