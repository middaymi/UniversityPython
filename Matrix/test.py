
from Matrix import Matrix


class SquareMatrix(Matrix):
    def pow(self, other):
        if other < 0:
            return 'You enter the wrong degree'
        if other == 0:
            self.res = [[0 for r in range(self.column)] for c in range(self.row)]
            for i in range(self.row):
                for j in range(self.column):
                    if i == j:
                        self.res[i][i] = 1
                    else:
                        self.res[i][j] = 0
            return "The exponentiation \n" + "\n".join(['\t'.join([str(item) for item in row]) for row in self.res])
        if other > 0:
            if self.row == self.column:
                self.res = self.matrix
                for n in range(1, other):
                    self.tmpMatrix = [[0 for r in range(self.column)] for c in range(self.row)]
                    for i in range(self.row):
                        for j in range(self.column):
                            for k in range(0, self.column):
                                self.tmpMatrix[i][j] += self.res[i][k] * self.matrix[k][j]
                    self.res = self.tmpMatrix
            else:
                return "You enter the wrong matrix, it should be square"
        return "The exponentiation \n" + "\n".join(['\t'.join([str(item) for item in row]) for row in self.res])


matr4 = SquareMatrix([[4, 6, 7], [3, 2, 1], [2, 3, 2]])
print("Matrix 4\n", matr4)
print(matr4 ** 3)