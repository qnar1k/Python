import random
def generate_random_matrix(rows, cols):    return [[random.randint(1, 100) for _ in range(cols)] for _ in range(rows)]
def get_column_sum(matrix, col_index):
    return sum(row[col_index] for row in matrix)
def get_row_average(matrix, row_index):
    return sum(matrix[row_index]) / len(matrix[row_index])
def main():    rows, cols = 5, 4
    matrix = generate_random_matrix(rows, cols)    
    print("Generated Matrix:")    for row in matrix:
        print(row)    
    col_index = 1    col_sum = get_column_sum(matrix, col_index)
    print(f"\nSum of column {col_index}: {col_sum}")    
    row_index = 2    row_avg = get_row_average(matrix, row_index)
    print(f"Average of row {row_index}: {row_avg}")
main()
