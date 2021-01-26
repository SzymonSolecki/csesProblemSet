n = int(input())

a = []

for i in range(2**n):
    u = i ^ (i >> 1)
    a.append(f'{u:b}'.zfill(n))

print(*a)
