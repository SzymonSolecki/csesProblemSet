n = int(input())

target = ((1 + n)/2)*n

a = []
b = []

if target % 2 == 0:
    for i in range(n, 0, -4):
        a.append(i)
        b.append(i - 1)
        b.append(i - 2)
        a.append(i - 3)

    if n%2 == 1:
        a.pop()
    print("YES", len(a), *a, len(b), *b)
else:
    print("NO")
