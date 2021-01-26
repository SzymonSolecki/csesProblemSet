dna_sequence = input()

longest_sequence = 0
current_longest_sequence = 0

prev_char = None

for char in dna_sequence:
    if char == prev_char:
        current_longest_sequence += 1
    else:
        current_longest_sequence = 1

    if current_longest_sequence > longest_sequence:
        longest_sequence = current_longest_sequence

    prev_char = char

print(longest_sequence)
