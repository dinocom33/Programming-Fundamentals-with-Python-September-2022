def unpack(s):
    return "".join(map(str, s))


message = input()
commands = input()

message_list = list(message)

while commands != "Decode":
    command = commands.split("|")
    if command[0] == "Move":
        for index in range(int(command[1])):
            message_list += message_list.pop(0)
    elif command[0] == "Insert":
        message_list.insert(int(command[1]), command[2])
    elif command[0] == "ChangeAll":
        for element in range(len(message_list)):
            if message_list[element] == command[1]:
                message_list[element] = command[2]

    commands = input()

print(f"The decrypted message is: {unpack(message_list)}")
