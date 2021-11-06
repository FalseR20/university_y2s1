import itertools


def pr(self, *args):
    return [el for el in itertools.product(self, *args)]


a = {1, 2}
b = {2, 3}
print(pr(a, a, b))
