import random
class Matrix:    def __init__(self, rows, cols):
        self.rows = rows        self.cols = cols
        self.matrix = [[random.randint(1, 10) for _ in range(cols)] for _ in range(rows)]
    def __str__(self):
        return "\n".join([" ".join(map(str, row)) for row in self.matrix])
    def __add__(self, other):        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("Matrices must have the same dimensions for addition.")        result = Matrix(self.rows, self.cols)
        result.matrix = [            [self.matrix[i][j] + other.matrix[i][j] for j in range(self.cols)]
            for i in range(self.rows)        ]
        return result
    def __sub__(self, other):        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("Matrices must have the same dimensions for subtraction.")        result = Matrix(self.rows, self.cols)
        result.matrix = [            [self.matrix[i][j] - other.matrix[i][j] for j in range(self.cols)]
            for i in range(self.rows)        ]
        return result
    def __mul__(self, other):        if self.cols != other.rows:
            raise ValueError("Number of columns of the first matrix must equal the number of rows of the second matrix.")        result = Matrix(self.rows, other.cols)
        result.matrix = [            [sum(self.matrix[i][k] * other.matrix[k][j] for k in range(self.cols)) for j in range(other.cols)]
            for i in range(self.rows)        ]
        return result
if name == "__main__":
    print("Matrix A:")    mat_a = Matrix(3, 3)
    print(mat_a)
    print("\nMatrix B:")    mat_b = Matrix(3, 3)
    print(mat_b)
    print("\nMatrix A + Matrix B:")    mat_sum = mat_a + mat_b
    print(mat_sum)
    print("\nMatrix A - Matrix B:")    mat_diff = mat_a - mat_b
    print(mat_diff)
    print("\nMatrix A * Matrix B:")
    mat_prod = mat_a * mat_b    print(mat_prod)
