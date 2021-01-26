n = int(input())
N = 1000000007

ans = 1

for i in range(n):
    ans = ans * 2 % N

print(ans)
