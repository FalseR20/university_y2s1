from pprint import pprint
from functions import *


def main():
    u = [i + 1 for i in range(11)]
    a = [1, 2, 3, 4, 6, 9]
    b = [3, 4, 5, 8, 9]
    c = [5, 6, 7, 9]

    print('Задание 1 Вариант 9')

    print('\n1. Булеан A:')
    pprint(boolean(a))

    print('\n2а. Сортировка слиянием:')
    pprint(merge_sort([3, 5, 4, 6, 2, 7, 1, 8, 9, 0]))

    print('\n2б. Слияние (A ∨ B):')
    pprint(merge(a, b, u))

    print('\n3. Прямое произведение (A ✕ B):')
    direct_multiply_ab = direct_multiply(a, b)
    pprint(direct_multiply_ab)
    print(f'Мощностью {len(direct_multiply_ab)}')

    print('\n4. Вычисление выражения A ∩ (B ∆ C):')
    pprint(intersect(a, symmetric_difference(b, c, u), u))
    print('Битовая маска:')
    pprint(intersect_mask(bit_mask(a, u), symmetric_difference_mask(bit_mask(b, u), bit_mask(c, u))))


if __name__ == '__main__':
    main()
