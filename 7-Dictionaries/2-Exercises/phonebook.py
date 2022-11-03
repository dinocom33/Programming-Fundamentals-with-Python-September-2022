command = input()

phonebook = {}

while not command.isnumeric():
    contact = command.split("-")
    name, number = contact[0], contact[1]
    if name not in phonebook:
        phonebook[name] = 0
    phonebook[name] = number
    command = input()

for i in range(int(command)):
    command = input()
    if command in phonebook.keys():
        print(f"{command} -> {phonebook[command]}")
    else:
        print(f"Contact {command} does not exist.")
