import numpy as np


def adjacency_matrix(ribs: list[tuple]) -> np.ndarray:
    count = np.max(ribs) + 1
    m = np.zeros((count, count), dtype=np.int32)
    for a, b in ribs:
        m[a][b] = m[b][a] = 1
    return m


def encoding(matrix: np.ndarray) -> list:
    count = len(matrix)
    code = []
    for _ in range(count - 2):
        for i, row in enumerate(matrix):
            if np.sum(row) == 1:
                j = row.argmax()
                code.append(j)
                matrix[i][j] = matrix[j][i] = 0
                break
    return code


def decoding(code: list) -> np.ndarray:
    count = len(code) + 2
    m = np.zeros((count, count), dtype=np.int32)
    range_ = np.arange(count)

    while code:
        for i_el, el in enumerate(range_):
            if el not in code:
                # print(f"--- {code[0]}-{el} ---", code, range_, sep="\n")
                m[el][code[0]] = m[code[0]][el] = 1
                code.pop(0)
                range_ = np.delete(range_, i_el)
                break
    # print(f"--- {range_[0]}-{range_[1]} ---")
    m[range_[0]][range_[1]] = m[range_[1]][range_[0]] = 1
    return m


def main():
    ribs = [(0, 1), (0, 2), (1, 3), (1, 4), (2, 5), (2, 6), (5, 7), (7, 8), (7, 9), (8, 10)]
    matrix = adjacency_matrix(ribs)
    print("Matrix:", matrix, sep="\n")
    code = encoding(matrix)
    print(f"Code: {code}")
    matrix_decoded = decoding(code)
    print("Matrix decoded:", matrix_decoded, sep="\n")


if __name__ == '__main__':
    main()
