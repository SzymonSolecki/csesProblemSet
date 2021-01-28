n = int(input())
apples = [int(x) for x in input().split()]
apples.sort(reverse=True)

h1 = 0
h2 = 0

for apple in apples:
    if h1 < h2:
        h1 += apple
    else:
        h2 += apple

print(abs(h1 - h2))
