import re
from copy import copy


def print_matrix(printed):
    for i in range(0, len(printed)):
        print(re.sub('[[]|[]]', '', str(printed[i]).strip()).replace(", ", "   "))


def change_row_column(cahnged_matrix):
    new_matrix = []
    tmplst = []
    for j in range(0, len(cahnged_matrix)):
        for i in range(0, len(cahnged_matrix)):
            tmplst.append(cahnged_matrix[i][j])
        new_matrix.append(copy(tmplst))
        tmplst.clear()
    return new_matrix


matrix = [[1, 2, 3, 5], [1, 2, 3, 4], [3, 2, 3, 1], [3, 2, 1, 3]]
matrix = sorted(change_row_column(matrix), key=lambda x: x[0], reverse=True)
print_matrix(change_row_column(matrix))