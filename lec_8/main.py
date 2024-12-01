import random
class Matrix:    def __init__(self, n, m):
        self.rows = n        self.cols = m
        self.matrix = [[random.randint(1, 100) for _ in range(m)] for _ in range(n)]    
    def print_matrix(self):        print("Matrix:")
        for row in self.matrix:            print(row)
        def calculate_mean(self):
        total_sum = sum(sum(row) for row in self.matrix)        total_elements = self.rows * self.cols
        return total_sum / total_elements
    def row_sum(self, row):
        if 0 <= row < self.rows:            return sum(self.matrix[row])
        else:            raise ValueError("Invalid row index.")
    def column_average(self, col):

        if 0 <= col < self.cols:            col_sum = sum(self.matrix[i][col] for i in range(self.rows))
            return col_sum / self.rows        else:
            raise ValueError("Invalid column index.")
    def print_submatrix(self, col1, col2, row1, row2):
        if 0 <= row1 <= row2 < self.rows and 0 <= col1 <= col2 < self.cols:            print("Submatrix:")
            for i in range(row1, row2 + 1):                print(self.matrix[i][col1:col2 + 1])
        else:            raise ValueError("Invalid submatrix indices.")

if name == "__main__":    # Create a 4x5 matrix
    mat = Matrix(4, 5)    mat.print_matrix()
    print(f"Mean of the matrix: {mat.calculate_mean():.2f}")    print(f"Sum of row 2: {mat.row_sum(1)}")
    print(f"Average of column 3: {mat.column_average(2):.2f}")    mat.print_submatrix(1, 3, 1, 2)  # Submatrix from columns 1 to 3 and rows 1 to 2
