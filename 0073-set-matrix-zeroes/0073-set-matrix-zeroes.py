class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows, cols = len(matrix), len(matrix[0])
        row_1 = False

        # Step 1: Mark rows and columns that need to be zeroed
        for r in range(rows):
            for c in range(cols):
                if matrix[r][c] == 0:
                    matrix[0][c] = 0  # Mark the column
                    if r > 0:
                        matrix[r][0] = 0  # Mark the row
                    else:
                        row_1 = True  # First row needs to be zeroed later

        # Step 2: Use the marks to zero out the cells (except the first row/col)
        for r in range(1, rows):
            for c in range(1, cols):
                if matrix[0][c] == 0 or matrix[r][0] == 0:
                    matrix[r][c] = 0

        # Step 3: Zero out the first column if needed
        if matrix[0][0] == 0:
            for r in range(rows):
                matrix[r][0] = 0

        # Step 4: Zero out the first row if needed
        if row_1:
            for c in range(cols):
                matrix[0][c] = 0