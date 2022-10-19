initial_list = input().split("!")

command = input()

while command != "Go Shopping!":
    current_command = command.split(" ")
    action = current_command[0]
    item = current_command[1]
    if action == "Urgent":
        if item not in initial_list:
            initial_list.insert(0, item)
    elif action == "Unnecessary":
        if item in initial_list:
            initial_list.remove(item)
    elif action == "Correct":
        new_item = current_command[2]
        if item in initial_list:
            initial_list = list(map(lambda x: x.replace(item, new_item), initial_list))
    elif action == "Rearrange":
        if item in initial_list:
            temp_item = initial_list.pop(initial_list.index(item))
            initial_list.append(temp_item)
    command = input()

print(", ".join(initial_list))
