n = int(input())
n_sum = ((1 + n)/2)*n

numbers = [int(x) for x in input().split()]
sum_of_numbers = sum(numbers)

print(int(n_sum - sum_of_numbers))
