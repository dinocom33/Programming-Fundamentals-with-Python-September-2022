command = input()

dictionary = {}
line = 1
key = ""

while command != "stop":
    if line % 2 != 0:
        key = command
        if command not in dictionary.keys():
            dictionary[key] = 0
    else:
        dictionary[key] += int(command)
    line += 1
    command = input()

[print(f"{key} -> {dictionary[key]}") for (key) in dictionary]
