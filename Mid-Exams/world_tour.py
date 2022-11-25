def valid_index(index):
    if 0 <= index < len(stops):
        return True
    return False


def add_stop(stops, index, string):
    if valid_index(index):
        stops = stops[:index] + string + stops[index:]
    return stops


def remove_stop(stops, start, end):
    if valid_index(start) and valid_index(end):
        stops = stops[:start_index] + "" + stops[end_index + 1:]
    return stops


def switch(stops, old, new):
    if old in stops:
        stops = stops.replace(old, new)
    return stops


stops = input()

command = input()

while command != "Travel":
    current_command = command.split(":")
    action = current_command[0]
    if action == "Add Stop":
        index = int(current_command[1])
        add_string = current_command[2]
        stops = add_stop(stops, index, add_string)
    elif action == "Remove Stop":
        start_index = int(current_command[1])
        end_index = int(current_command[2])
        stops = remove_stop(stops, start_index, end_index)
    elif action == "Switch":
        old_string = current_command[1]
        new_string = current_command[2]
        stops = switch(stops, old_string, new_string)
    print(stops)
    command = input()

print(f"Ready for world tour! Planned stops: {stops}")
