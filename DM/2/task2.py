def transpose(matrix: list[list]) -> list[list]:
    """Транспонирование матрицы для обратного отношения"""
    output = [list(column) for column in zip(*matrix)]
    return output


class Space:
    def __init__(self, rb: range, rc: range, s: list[tuple]) -> None:
        self.b = rb
        self.c = rc
        self.s = s
        self.relation_matrix(s)

    def relation_matrix(self, boolean: list[tuple]) -> None:
        """Построение матрицы по булеану"""
        self.m = [[0 for _ in self.c] for _ in self.b]
        for i, j in boolean:
            self.m[i - self.b[0]][j - self.c[0]] = 1

    def pprint(self) -> None:
        """Красивый вывод матрицы"""
        print(' ', *self.c, sep='  ')
        for i, im in enumerate(self.b):
            print(im, self.m[i])

    def is_function(self) -> bool:
        """Является ли отношение функцией"""
        for row in self.m:
            if sum(row) != 1:
                return False
        return True

    def is_injective(self) -> bool:
        """Является ли функция инъективной"""
        for row in transpose(self.m):
            if sum(row) > 1:
                return False
        return True

    def is_surjective(self) -> bool:
        """Является ли функция сюръективной"""
        for row in transpose(self.m):
            if sum(row) == 0:
                return False
        return True

    def is_bijective(self) -> bool:
        """Является ли функция биективной"""
        return self.m == transpose(self.m)

    def test(self) -> None:
        self.pprint()
        is_function = self.is_function()
        print(f'Функция: {is_function}')
        if is_function:
            print(f'Инъекция: {self.is_injective()}')
            print(f'Сюръекция: {self.is_surjective()}')
            print(f'Биекция: {self.is_bijective()}')
        print()


def main():
    print('Оригинал:')
    rb = range(1, 5)
    rc = range(5, 9)
    s = [(1, 5), (2, 7), (3, 6), (4, 8)]
    sp = Space(rb, rc, s)
    sp.test()

    print('Даны на паре:\n')

    rb = range(1, 6)
    rc = range(6, 10)
    s = [(1, 6), (2, 6), (3, 7), (4, 7), (5, 8)]
    sp = Space(rb, rc, s)
    sp.test()

    rb = range(1, 5)
    rc = range(5, 8)
    s = [(1, 5), (2, 6), (3, 7), (4, 7)]
    sp = Space(rb, rc, s)
    sp.test()

    rb = range(1, 5)
    rc = range(5, 9)
    s = [(1, 7), (2, 5), (2, 6), (3, 8), (4, 7)]
    sp = Space(rb, rc, s)
    sp.test()

    # rb = range(1, 5)
    rc = range(5, 10)
    s = [(1, 6), (2, 5), (3, 7), (4, 9)]
    sp = Space(rb, rc, s)
    sp.test()

    rb = range(1, 4)
    rc = range(4, 7)
    s = [(1, 4), (2, 5), (3, 6)]
    sp = Space(rb, rc, s)
    sp.test()


if __name__ == '__main__':
    main()
