# Write a Python function that takes a 2D list (matrix) and returns its transpose.



def transpose_matrix(matrix):
    return [list(row) for row in zip(*matrix)]

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(transpose_matrix(matrix))
