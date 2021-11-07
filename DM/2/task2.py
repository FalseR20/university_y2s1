from task1 import transpose


def relation_matrix(boolean: list[tuple]) -> list[list]:
    """Построение матрицы по булеану"""
    output = [[0 for _ in R4] for _ in R4]
    for i, j in boolean:
        output[i - 1][j - 5] = 1
    return output


def pprint(m):
    """Красивый вывод матрицы"""
    print('   5  6  7  8')
    for i, row in enumerate(m):
        print(i + 1, row)


def is_function(m: list[list]) -> bool:
    """Является ли отношение функцией"""
    for row in m:
        if sum(row) > 1:
            return False
    return True


def is_injective(m):
    """Является ли функция инъективной"""
    for row in transpose(m):
        if sum(row) > 1:
            return False
    return True


def is_surjective(m):
    """Является ли функция сюръективной"""
    for row in transpose(m):
        if sum(row) == 0:
            return False
    return True


def is_bijective(m):
    """Является ли функция биективной"""
    return m == transpose(m)


B = [1, 2, 3, 4]
C = [5, 6, 7, 8]
S = [(1, 5), (2, 7), (3, 6), (4, 8)]

R4 = range(4)

matrix = relation_matrix(S)
pprint(matrix)
is_f = is_function(matrix)
print(f'Является ли отношение функцией: {is_f}')
if is_f:
    print(f'''Инъекция: {is_injective(matrix)}
Сюръекция: {is_surjective(matrix)}
Биекция: {is_bijective(matrix)}
''')
