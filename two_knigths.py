from itertools import combinations


for k in range(1, int(input()) + 1):
    if k == 1:
        print(0)
    else:
        comb = ((k**2) * (k**2 - 1)) / 2
        number_of_attack_positions = 4 * ((k - 1)*(k - 2))

        print(int(comb - number_of_attack_positions))
