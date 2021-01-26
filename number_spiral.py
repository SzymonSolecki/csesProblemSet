def find_number(x, y):
    max_n, min_n = max(x, y), min(x, y)
    diagonal_number = max_n**2 - max_n + 1

    multiplier = [-1, 1][max_n % 2]

    diff = max_n - min_n
    diff *= multiplier

    return diagonal_number + diff if max_n == y else diagonal_number - diff


for _ in range(int(input())):
    x, y = [int(n) for n in input().split()]
    print(find_number(x, y))
