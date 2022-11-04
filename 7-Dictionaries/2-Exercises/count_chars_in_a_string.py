initial_input = input().split()
symbols = "".join(initial_input)

letters = {}

for current_symbol in symbols:
    if current_symbol not in letters.keys():
        letters[current_symbol] = 0
    letters[current_symbol] += 1

for letter, occurrences in letters.items():
    print(f"{letter} -> {occurrences}")
