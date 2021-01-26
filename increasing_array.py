n = int(input())
array = [int(x) for x in input().split()]

number_of_moves = 0
prev_number = -1

for number in array:
    if number < prev_number:
        number_of_moves += prev_number - number
        number = prev_number
    prev_number = number

print(number_of_moves)
