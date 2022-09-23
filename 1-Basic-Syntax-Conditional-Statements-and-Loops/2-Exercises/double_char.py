command = input()

while command != "End":
    new_word = ""
    if command != "SoftUni":
        for letter in command:
            new_word += letter + letter
        print(new_word)
    command = input()
