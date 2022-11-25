def valid_index(index):
    if 0 <= index < len(all_stops):
        return True
    return False


def add_stop(stops, index, string):
    if valid_index(index):
        stops = stops[:index] + string + stops[index:]
    return stops


def remove_stop(stops, start, end):
    if valid_index(start) and valid_index(end):
        stops = stops[:start] + "" + stops[end + 1:]
    return stops


def switch_stops(stops, old, new):
    if old in stops:
        stops = stops.replace(old, new)
    return stops


all_stops = input()

while True:
    command = input()
    if command == "Travel":
        break

    current_command = command.split(":")
    action = current_command[0]
    if action == "Add Stop":
        index = int(current_command[1])
        string_to_add = current_command[2]
        all_stops = add_stop(all_stops, index, string_to_add)
        print(all_stops)
    elif action == "Remove Stop":
        start_index = int(current_command[1])
        end_index = int(current_command[2])
        all_stops = remove_stop(all_stops, start_index, end_index)
        print(all_stops)
    elif action == "Switch":
        old_string = current_command[1]
        new_string = current_command[2]
        all_stops = switch_stops(all_stops, old_string, new_string)
        print(all_stops)

print(f"Ready for world tour! Planned stops: {all_stops}")
