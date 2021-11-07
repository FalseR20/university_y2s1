# Вариант 9

import itertools
import numpy as np
from copy import deepcopy
from pprint import pprint
from typing import Callable

A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
N = 10
RN = range(N)


def r1(x: int, y: int) -> bool:
    """Отношение R1: (a + b) - четное число"""
    return (x + y) % 2 == 0


def r2(x: int, y: int) -> bool:
    """Отношение R2: (a + b) < 7"""
    return (x + y) < 7


def relation_boolean(s: list, r: Callable[[int, int], bool]) -> list[tuple]:
    """Булеан отношения"""
    return [pare for pare in itertools.product(s, s) if r(pare[0], pare[1])]


def relation_matrix(s: list, r: Callable[[int, int], bool]) -> list[list]:
    """Матрица отношения"""
    boolean = relation_boolean(s, r)
    output = [[0 for _ in RN] for _ in RN]
    for i, j in boolean:
        output[i - 1][j - 1] = 1
    return output


def transpose(matrix: list[list]) -> list[list]:
    """Транспонирование матрицы для обратного отношения"""
    output = [list(column) for column in zip(*matrix)]
    return output


def addition(matrix: list[list]) -> list[list]:
    """Дополнение отношения"""
    output = [[1 for _ in RN] for _ in RN]
    for i, row in enumerate(matrix):
        for j, column in enumerate(row):
            output[i][j] ^= column
    return output


def warshall(matrix):
    """Алгоритм Флойда-Уоршолла"""
    matrix = deepcopy(matrix)
    for k in RN:
        for i in RN:
            for j in RN:
                matrix[i][j] |= matrix[i][k] and matrix[k][j]
    return matrix


def dot(m1: list[list], m2: list[list]):
    """Произведение матриц для композиции"""
    output = [[0 for _ in RN] for _ in RN]
    for i in RN:
        for j in RN:
            for k in RN:
                output[i][j] |= m1[i][k] and m2[k][j]
    return output


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
    pprint(warshall(matrix2))

    print('\n5. Композиция:\nR ○ S')
    pprint(dot(matrix1, matrix2))
    print('\nS ○ R')
    pprint(dot(matrix2, matrix1))
    print('\nСвойством коммутативности не обладает')


if __name__ == '__main__':
    main()
