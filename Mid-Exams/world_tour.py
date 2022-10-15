stops = input().split()

stops_list = [elem for el in stops for elem in el]
result = ""
while True:
    command = input()

    if command == "Travel":
        break

    current_command = command.split(":")
    action = current_command[0]

    if action == "Add Stop":
        index = int(current_command[1])
        string = [elem for el in current_command[2] for elem in el]
        stops_list[index:len(string)] = string
        print(*stops_list, sep="")
    elif action == "Remove Stop":
        start_index = int(current_command[1])
        end_index = int(current_command[2])
        if start_index <= len(stops_list) and end_index <= len(stops_list):
            for ind in range(end_index, start_index - 1, -1):
                del stops_list[ind]
            print(*stops_list, sep="")
    elif action == "Switch":
        old_string = current_command[1]
        new_string = current_command[2]
        stops_list = str("".join((stops_list[::])))
        if old_string in stops_list:
            result = stops_list.replace(old_string, new_string)
        print(*result, sep="")

print(f"Ready for world tour! Planned stops: {result}")
