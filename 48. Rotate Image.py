class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
       
       matrix_size = len(matrix)

       for row_index in range(matrix_size // 2):
        for col_index in range((matrix_size + 1) // 2):
            # Save top left starting cell
            saved_TL = matrix[row_index][col_index]
            # Bottom left --> top left
            matrix[row_index][col_index] = matrix[matrix_size -1 - col_index][row_index]
            # Bottom right --> bottom left
            matrix[matrix_size - 1 - col_index][row_index] = matrix[matrix_size -1 - row_index][matrix_size - 1 - col_index]
            # Top right --> bottom right
            matrix[matrix_size -1 - row_index][matrix_size - 1 - col_index] = matrix[col_index][matrix_size -1 - row_index]

            # Saved Top left --> top right
            matrix[col_index][matrix_size -1 - row_index] = saved_TL
