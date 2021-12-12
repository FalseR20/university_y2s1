import numpy as np


def prim(matrix: np.ndarray) -> list:
    roots = [0]
    tuples = []
    while len(roots) < len(matrix):
        min_el = min_i = min_j = np.inf
        for root in roots:
            for j, weight in enumerate(matrix[root]):
                if 0 < weight < min_el and j not in roots:
                    min_el = weight
                    min_i = root
                    min_j = j
        roots.append(min_j)
        tuples.append((min_i, min_j))
    return tuples


def main():
    matrix = np.array([
        [0, 5, 2, 3, 0, 0],
        [5, 0, 0, 3, 0, 0],
        [2, 0, 0, 2, 6, 0],
        [3, 3, 2, 0, 7, 5],
        [0, 0, 6, 7, 0, 4],
        [0, 0, 0, 5, 4, 0],
    ])
    print("Default matrix:", matrix, sep='\n')
    print("Ost tree prim:", prim(matrix), sep='\n')


if __name__ == '__main__':
    main()
