for _ in range(int(input())):
    a, b = sorted([int(x) for x in input().split()])

    if (a+b) % 3 or b > a * 2:
        print("NO")
    else:
        print("YES")
