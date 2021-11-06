import itertools
from pprint import pprint

A = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}


# Вариант 9
def r1(x, y) -> bool:
    """Отношение R1: (a+b) - четное число"""
    return (x + y) % 2 == 0


def r2(x, y) -> bool:
    """Отношение R2: (a + b) < 7"""
    return (x + y) < 7


# def relation_matrix(A, B, )


class MySet(set):
    @staticmethod
    def mul(self, *args: set):
        return [el for el in itertools.product(self, *args)]

    # def __pow__(self, y):
    #     return


print('Задание 1')

ms = MySet({1, 2})
print(ms * ms * ms)

# print()
