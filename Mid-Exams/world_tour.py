stops = input()

while True:
    command = input()

    if command == "Travel":
        break

    current_command = command.split(":")
    action = current_command[0]

    if action == "Add Stop":
        index = int(current_command[1])
        string = current_command[2]
        stops = stops[:index] + string + stops[index:]
        print(stops)
    elif action == "Remove Stop":
        start_index = int(current_command[1])
        end_index = int(current_command[2])
        stops = stops[:start_index] + stops[end_index + 1:]
        print(stops)
    elif action == "Switch":
        old_string = current_command[1]
        new_string = current_command[2]
        if old_string in stops:
            stops = stops.replace(old_string, new_string)
        print(stops)

print(f"Ready for world tour! Planned stops: {stops}")
