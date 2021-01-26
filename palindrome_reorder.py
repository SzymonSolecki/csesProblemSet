n = input()

def is_possible(dic):

    odd_found = False
    for value in dic.values():
        if value % 2 == 1 and odd_found:
            return False
        elif value % 2 == 1:
            odd_found = True

    return True

def get_palindrome(seq):
    letters = {}

    for letter in seq:
        letters[letter] = letters.get(letter, 0) + 1

    if not is_possible(letters):
        return "NO SOLUTION"

    arr = []
    middle_letter = None

    for key, value in letters.items():
        if value%2 == 0:
            arr.append(key * (value//2))
        elif value//2 != 0:
            arr.append(key * (value//2))
            middle_letter = key
        else:
            middle_letter = key

    tmp = arr[::-1]
    if middle_letter:
        arr += middle_letter
    arr += tmp

    return arr

print(*get_palindrome(n), sep='')
