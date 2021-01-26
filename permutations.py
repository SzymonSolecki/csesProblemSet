n = int(input())

if n == 1:
    print(1)
elif n <= 3:
    print("NO SOLUTION")
else:
    if n % 2 == 0:
        [print(x) for x in range(n - 1, 0, -2)]
        [print(x) for x in range(n, 1, -2)]
    else:
        [print(x) for x in range(n - 1, 1, -2)]
        [print(x) for x in range(n, 0, -2)]
