from typing import List


# ___Стандартные операции с множествами___
def bit_mask(x: List[int], u: List[int]) -> List[bool]:
    """Получение битовой маски"""
    out: list[bool] = []
    for el in u:
        out.append(x.count(el) > 0)
    return out


def merge(x: List[int], y: List[int], u: List[int]) -> List[int]:
    """Слияние двух множеств"""
    out = []
    for el in u:
        if x.count(el) + y.count(el) >= 1:
            out.append(el)
    return out


def merge_mask(x: list[bool], y: list[bool]) -> list[bool]:
    """Слияние двух множеств битовой маской"""
    out: list[bool] = []
    for el in range(len(x)):
        out.append(x[el] + y[el] >= 1)
    return out


def intersect(x: List[int], y: List[int], u: List[int]) -> List[int]:
    """Пересечение двух множеств"""
    out = []
    for el in u:
        if x.count(el) + y.count(el) >= 2:
            out.append(el)
    return out


def intersect_mask(x: list[bool], y: list[bool]) -> list[bool]:
    """Пересечение двух битовых масок"""
    out: list[bool] = []
    for el in range(len(x)):
        out.append(x[el] + y[el] >= 2)
    return out


def symmetric_difference(x: List[int], y: List[int], u: List[int]) -> List[int]:
    """Симметрическая разность"""
    out = []
    for el in u:
        if x.count(el) + y.count(el) == 1:
            out.append(el)
    return out


def symmetric_difference_mask(x: list[bool], y: list[bool]) -> list[bool]:
    """Симметрическая разность двух битовых масок"""
    out: list[bool] = []
    for el in range(len(x)):
        out.append(x[el] + y[el] == 1)
    return out


# ___Другие операции с множествами___
def boolean(inp: list[int]) -> List[List[int]]:
    """Получение булеана"""
    times = 2 ** len(inp)
    out = []
    for time in range(times):
        temp = []
        for i in range(len(inp)):
            if time % 2 == 1:
                temp.append(inp[i])
            time //= 2
        out += [temp]
    return out


def merge_sort(inp: List[int]) -> List[int]:
    """Сортировка слиянием"""
    inp_len = len(inp)
    if inp_len == 1:
        return inp

    else:
        inp_half_len = inp_len // 2
        left = merge_sort(inp[:inp_half_len])
        right = merge_sort(inp[inp_half_len:])
        out = []
        i, j = 0, 0
        while i < inp_half_len and j < inp_len - inp_half_len:
            if left[i] < right[j]:
                out.append(left[i])
                i += 1
            else:
                out.append(right[j])
                j += 1
        if i != inp_half_len:
            out += left[i:]
        elif j != inp_len - inp_half_len:
            out += right[j:]
        return out


def direct_multiply(x: List[int], y: List[int]) -> List[List[int]]:
    """Прямое произведение"""
    out = []
    for xi in x:
        for yi in y:
            out.append([xi, yi])
    return out
