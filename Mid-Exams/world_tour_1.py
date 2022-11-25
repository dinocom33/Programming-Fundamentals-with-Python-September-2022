def valid_index(index_to_validate):
    if 0 <= index_to_validate < len(all_stops):
        return True
    return False


def add_stop(stops, given_index, string):
    if valid_index(given_index):
        stops = stops[:given_index] + string + stops[given_index:]
    return stops


def remove_stop(stops, start, end):
    if valid_index(start) and valid_index(end):
        stops = stops[:start] + stops[end + 1:]
    return stops


def switch_stops(stops, old, new):
    if old in stops:
        stops = stops.replace(old, new)
    return stops


all_stops = input()

while True:
    command = input().split(":")
    action = command[0]
    if action == "Travel":
        break

    if action == "Add Stop":
        index = int(command[1])
        string_to_add = command[2]
        all_stops = add_stop(all_stops, index, string_to_add)
    elif action == "Remove Stop":
        start_index = int(command[1])
        end_index = int(command[2])
        all_stops = remove_stop(all_stops, start_index, end_index)
    elif action == "Switch":
        old_string = command[1]
        new_string = command[2]
        all_stops = switch_stops(all_stops, old_string, new_string)
    print(all_stops)

print(f"Ready for world tour! Planned stops: {all_stops}")
