gift_names = input().split()

command = input().split()
command_as_string = " ".join([str(element) for element in command])

while command_as_string != "No Money":
    if "OutOfStock" in command:
        for index in range(len(gift_names)):
            if gift_names[index] == command[1]:
                gift_names[index] = "None"
    elif "Required" in command:
        if 0 <= int(command[2]) < len(gift_names):
            gift_names[int(command[2])] = command[1]
    elif "JustInCase" in command:
        gift_names[-1] = command[1]
    command = input().split()
    command_as_string = " ".join([str(element) for element in command])

for index_value in gift_names:
    if index_value == "None":
        gift_names.remove("None")

print(*gift_names, sep=" ")
