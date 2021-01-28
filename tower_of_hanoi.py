n = int(input())
print(2**n - 1)


def TOH(n, a, b, c):
    if n > 0:
        TOH(n - 1, a, c, b)
        print(a, c)
        TOH(n - 1, b, a, c)

TOH(n, 1, 2, 3)
