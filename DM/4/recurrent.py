def recurrent_relation(n):
    if n >= 2:
        return -recurrent_relation(n - 1) + recurrent_relation(n - 2)
    if n == 1:
        return 2
    if n == 0:
        return 4


def recurrent_relation_formula(n):
    return (2 + 4 * 5 ** 0.5 / 5) * (-0.5 + 5 ** 0.5 / 2) ** n + \
           (2 - 4 * 5 ** 0.5 / 5) * (-0.5 - 5 ** 0.5 / 2) ** n


print(f"Recursive function: {recurrent_relation(5)}")
print(f"Formula: {recurrent_relation_formula(5)}")

# for i in range(10):
#     print(recurrent_relation(i), end=' ')
#     print(recurrent_relation_formula(i))
