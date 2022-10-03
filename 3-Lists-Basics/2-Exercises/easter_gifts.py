gift_names = input().split()

command = input()

while command != "No Money":
    command = command.split()
    if "OutOfStock" in command:
        for index in range(len(gift_names)):
            if gift_names[index] == command[1]:
                gift_names[index] = "None"
    elif "Required" in command:
        if 0 <= int(command[2]) < len(gift_names):
            gift_names[int(command[2])] = command[1]
    elif "JustInCase" in command:
        gift_names[-1] = command[1]
    command = input()

for index_value in gift_names[::-1]:
    if index_value == "None":
        gift_names.remove("None")

print(*gift_names, sep=" ")
