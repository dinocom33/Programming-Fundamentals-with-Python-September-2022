targets = list(map(int, input().split(" ")))

command = input()

while command != "End":
    current_command = command.split(" ")
    action = current_command[0]
    index = int(current_command[1])
    value = int(current_command[2])

    if action == "Shoot" and 0 <= index < len(targets):
        current_target = targets[index]
        current_target -= value
        if current_target <= 0:
            targets.pop(index)
        else:
            targets[index] = current_target

    elif action == "Add":
        if 0 <= index < len(targets):
            targets.insert(index, value)
        else:
            print("Invalid placement!")

    elif action == "Strike":
        if index - value >= 0 and index + value < len(targets):
            targets = targets[:index - value] + targets[index + value + 1:]
        else:
            print("Strike missed!")

    command = input()
output = list(map(str, targets))
print("|".join(output))
