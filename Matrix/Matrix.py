import copy
import re


class Matrix:

    def __init__(self, matrix):
        self.matrix = copy.deepcopy(matrix)
        self.row = len(self.matrix)
        self.column = len(self.matrix[0])

    def __str__(self):
        result = ""
        for row in self.matrix:
            result = result + (re.sub('[[]|[]]', '', str(row)).replace(", ", "\t") + "\n")
        return result.strip()

    # def __iter__(self):
    #     for el in self.matrix:
    #         yield el

    def matrix_size(self):
        return self.row, self.column

    def add(self, other):
        if self.matrix_size() != (len(other), len(other[0])):
            return "invalid size of error"
        self.result_matrix = copy.deepcopy(self.matrix)
        for i in range(self.row):
            for j in range(self.column):
                self.result_matrix[i][j] = self.matrix[i][j] + other[i][j]
        return self.result_matrix

    def mul(self, number):
        for i in range(self.row):
            for j in range(self.column):
                self.matrix[i][j] *= number
        return self.matrix

    def rmul(self, number):
        for i in range(self.row):
            for j in range(self.column):
                self.matrix[i][j] = number * self.matrix[i][j]
        return self.matrix








