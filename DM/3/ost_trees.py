import numpy as np


def prim(matrix: np.ndarray) -> list:
    roots = [0]
    ribs = []
    while len(roots) < len(matrix):
        min_el = min_i = min_j = np.inf
        for root in roots:
            for j, weight in enumerate(matrix[root]):
                if 0 < weight < min_el and j not in roots:
                    min_el = weight
                    min_i = root
                    min_j = j
        roots.append(min_j)
        ribs.append((min_i, min_j, min_el))
    return ribs


def kraskal(ribs, count):
    ost_ribs = []
    ribs.sort(key=lambda x: x[2])
    ribs_sets = [[i, ] for i in range(count)]
    while len(ribs_sets) > 1:
        i = j = -1
        k = 0
        while i == -1 or j == -1:
            if ribs[0][0] in ribs_sets[k]:
                i = k
            if ribs[0][1] in ribs_sets[k]:
                j = k
            k += 1
        new_set = ribs_sets[i] + ribs_sets[j]
        if len(set(new_set)) == len(new_set):
            ribs_sets[i] = new_set
            ribs_sets.pop(j)
            ost_ribs.append(ribs.pop(0))
        else:
            ribs.pop(0)
    return ost_ribs


def main():
    ribs = [(0, 1, 5), (0, 2, 2), (0, 3, 3), (1, 3, 3), (2, 3, 2), (2, 4, 6), (3, 4, 7), (3, 5, 5), (4, 5, 4)]
    roots_count = 6
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
    print("Ost tree kraskal:", kraskal(ribs, roots_count), sep='\n')


if __name__ == '__main__':
    main()
