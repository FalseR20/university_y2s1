import numpy as np


def adjacency_matrix(ribs: list[tuple]) -> np.ndarray:
    """Построение матрицы смежности"""
    count = np.max(ribs)
    m = np.zeros((count, count), dtype=np.int32)
    for a, b in ribs:
        m[a - 1][b - 1] = m[b - 1][a - 1] = 1
    return m


def print_pows(m: np.ndarray) -> None:
    """Вывод степеней вершин"""
    for i, row in enumerate(m):
        print(row, f"степень вершины #{i + 1}: {np.sum(row)}")


def delete(m: np.ndarray, row: np.ndarray) -> None:
    """Удаление прошедших вершин"""
    for i, bo in enumerate(row):
        if bo:
            row[i] = 0
            delete(m, m[i])


def connectivity_component(m: np.ndarray) -> int:
    """Компонент связанности"""
    count = 0
    for i, row in enumerate(m):
        if np.sum(row) > 0:
            count += 1
            delete(m, row)

    return count


def main():
    ribs = [(1, 2), (1, 3), (1, 4), (2, 3), (2, 4), (3, 4), (5, 7), (6, 8)]
    matrix = adjacency_matrix(ribs)
    print_pows(matrix)
    print(f"\nКомпонент связанности: {connectivity_component(matrix)}")


if __name__ == '__main__':
    main()
