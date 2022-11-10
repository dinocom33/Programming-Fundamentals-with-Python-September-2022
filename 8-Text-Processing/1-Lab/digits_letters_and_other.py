text = input()

digits = []
letters = []
others = []

for character in text:
    if character.isdigit():
        digits.append(character)
    elif character.isalpha():
        letters.append(character)
    else:
        others.append(character)

print("".join(digits))
print("".join(letters))
print("".join(others))
