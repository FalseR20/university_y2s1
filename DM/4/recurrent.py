def recurrent_relation(n):
    if n >= 2:
        return -recurrent_relation(n - 1) + recurrent_relation(n - 2)
    if n == 1:
        return 2
    if n == 0:
        return 4


print(recurrent_relation(5))

# for i in range(10):
#     print(recurrent_relation(i), end=' ')
