from Matrix import Matrix


class SquareMatrix(Matrix):

    def __init__(self, matrix):
        super().__init__(matrix)

    def __pow__(self, power):

        # matrix is not square
        if self.matrix_size()[0] != self.matrix_size()[1]:
            return "not square matrix"

        # illegal power
        if power < 0:
            return 'You enter the wrong degree'

        # if normal
        self.result_pow_matrix = Matrix(self.matrix)

        # unit matrix
        if power == 0:
            for i in range(self.row):
                for j in range(self.column):
                    self.result_pow_matrix.matrix[i][j] = (1 if i == j else 0)
            return self.result_pow_matrix

        # power > 0
        for n in range(1, power):
            self.tmpMatrix = Matrix([[0 for r in range(self.column)] for c in range(self.row)])
            for i in range(self.row):
                for j in range(self.column):
                    for k in range(0, self.column):
                        self.tmpMatrix.matrix[i][j] += self.result_pow_matrix.matrix[i][k] * self.matrix[k][j]
            self.result_pow_matrix = self.tmpMatrix
            return self.result_pow_matrix