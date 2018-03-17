from Matrix import Matrix
from SquareMatrix import SquareMatrix

input_matrix = [[2, 3, 4], [5, 6, 7], [8, 9, 10]]
added_matrix = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
square_matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

structure = Matrix(input_matrix)
print("MATRIX:\n", structure, "\n\nSIZE:\n", structure.matrix_size(), "\n\n", sep='', end='')

print("ADD:", added_matrix, "\n", Matrix(structure.add(added_matrix)), "\n\n", sep='', end='')

structure.mul(2)
print("MUL:\n", structure, "\n\n", sep='', end='')

structure.rmul(2.5)
print("RMUL:\n", structure, "\n\n", sep='', end='')

powered_matrix = SquareMatrix(square_matrix)
print("SQUARE MATRIX:\n", powered_matrix, "\n\nSIZE:\n", powered_matrix.matrix_size(), "\n\n", sep='', end='')

tmp_matrix = powered_matrix.__pow__(0)
print("POW0:\n", tmp_matrix, "\n\n", sep='', end='')

tmp_matrix = powered_matrix.__pow__(2)
print("POW2:\n", tmp_matrix, "\n\n", sep='', end='')

tmp_matrix = powered_matrix ** 2
print("POW2:\n", tmp_matrix, "\n\n", sep='', end='')

