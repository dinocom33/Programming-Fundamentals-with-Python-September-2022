targets = list(map(int, input().split(" ")))

command = input()

while command != "End":
    current_command = command.split(" ")
    action = current_command[0]
    index = int(current_command[1])
    if action == "Shoot":
        if 0 <= index < len(targets):
            power = int(current_command[2])
            if targets[index] - power <= 0:
                targets.pop(index)
            else:
                targets[index] -= power

    elif action == "Add":
        if 0 <= index < len(targets):
            value = current_command[2]
            targets.insert(index, value)
        else:
            print("Invalid placement!")
            
    elif action == "Strike":
        radius = int(current_command[2])
        index_validator = index - radius >= 0 and index + radius < len(targets)
        if index_validator:
            start_index = index - radius
            end_index = index + radius
            targets = [targets[i] for i in range(len(targets)) if i < start_index or i > end_index]
        else:
            print("Strike missed!")

    command = input()

print(*targets, sep="|")
