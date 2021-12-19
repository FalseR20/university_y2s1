def anti_lex_transpositions(arr, tail):
    if not arr:
        print(tail)
    for i in range(len(arr) - 1, -1, -1):
        anti_lex_transpositions(
            arr=arr[:i] + arr[i + 1:],
            tail=[arr[i]] + tail
        )


numbers = [1, 2, 3, 4]
anti_lex_transpositions(sorted(numbers), [])
