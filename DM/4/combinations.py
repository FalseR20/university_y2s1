def combinations(arr, n, head):
    if not n:
        print(head)
    else:
        for i in range(len(arr) - n + 1):
            combinations(arr[i + 1:], n - 1, head + [arr[i]])


m = int(input("Enter m (0 > m): "))
k = int(input(f"Enter k (0 > k >= {m}): "))

combinations(list(range(1, 1 + m)), k, [])
