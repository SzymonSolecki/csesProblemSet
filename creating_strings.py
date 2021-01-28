from itertools import permutations

n = input()

l = [''.join(x) for x in set(permutations(n))]
print(len(l))
print(*sorted(l))
