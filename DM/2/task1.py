# Вариант 9

import itertools
import numpy as np
from copy import deepcopy
from pprint import pprint
from typing import Callable

A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def r1(x: int, y: int) -> bool:
    """Отношение R1: (a + b) - четное число"""
    return (x + y) % 2 == 0


def r2(x: int, y: int) -> bool:
    """Отношение R2: (a + b) < 7"""
    return (x + y) < 7


def relation_boolean(s: list, r: Callable[[int, int], bool]) -> list[tuple]:
    return [arg for arg in itertools.product(s, s) if r(arg[0], arg[1])]


def relation_matrix(s: list, r: Callable[[int, int], bool]) -> list[list]:
    boolean = relation_boolean(s, r)
    output = [[0 for _ in s] for _ in s]
    for i, j in boolean:
        output[i - 1][j - 1] = 1
    return output


def transpose(matrix: list[list]) -> list[list]:
    output = [list(column) for column in zip(*matrix)]
    return output


def addition(matrix: list[list]) -> list[list]:
    output = [[1 for _ in row] for row in matrix]
    for i, row in enumerate(matrix):
        for j, column in enumerate(row):
            output[i][j] -= column
    return output


def auf(matrix):
    matrix = deepcopy(matrix)
    le = len(matrix)
    for k in range(le):
        for i in range(le):
            for j in range(le):
                matrix[i][j] |= matrix[i][k] and matrix[k][j]
    return matrix


def dot(m1: list[list], m2: list[list]):
    return np.dot(m1, m2).tolist()


def main():
    print('::ЗАДАНИЕ 1::\n1. Матрицы отношений:\nR1: (a + b) - четное число')
    matrix1 = relation_matrix(A, r1)
    pprint(matrix1)
    print('\nR2: (a + b) < 7')
    matrix2 = relation_matrix(A, r2)
    pprint(matrix2)

    print('\n2. Обратные отношения:\n(R1)^-1: (b + a) - четное число')
    pprint(transpose(matrix1))
    print('\n(R2)^-1: (b + a) < 7')
    pprint(transpose(matrix2))
    print('\nДополнения отношений:\n-R1: (a + b) - нечетное число')
    pprint(addition(matrix1))
    print('\n-R2: (a + b) >= 7')
    pprint(addition(matrix2))

    print('''3. Свойства отношений:
    R1: рефлексивно, симметрично, транзитивно -> эквивалентно, a ≡ b(mod 2)
    R2: симметрично''')

    print('\n4. Транзитивное замыкание алгоритмом Флойда-Уоршолла: R2')
    pprint(auf(matrix2))

    print('\n5. Композиция:\nR ○ S')
    pprint(dot(matrix1, matrix2))
    print('\nR ○ S')
    pprint(dot(matrix2, matrix1))


if __name__ == '__main__':
    main()
