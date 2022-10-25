def reverse_coffee(coffee_list):
    coffee_list.reverse()
    return coffee_list


def include_coffee(coffee_list, coffee):
    coffee_list.append(coffee)
    return coffee_list


def remove_coffee(coffee_list, first_last, index):
    if index < len(coffee_list):
        if first_last == "first":
            coffee_list = coffee_list[index:]
        elif first_last == "last":
            coffee_list = coffee_list[:-index]
    return coffee_list


def prefer_coffee(coffee_list, index1, index2):
    if index1 < len(coffee_list) and index2 < len(coffee_list):
        coffee_list[index1], coffee_list[index2] = coffee_list[index2], coffee_list[index1]
        return coffee_list


names_of_coffees = input().split(" ")
count_commands = int(input())

for command in range(count_commands):
    current_command = input().split(" ")
    action = current_command[0]
    if action == "Reverse":
        reverse_coffee(names_of_coffees)
    elif action == "Include":
        coffee_to_include = current_command[1]
        include_coffee(names_of_coffees, coffee_to_include)
    elif action == "Remove":
        first_last = current_command[1]
        coffee_index = int(current_command[2])
        names_of_coffees = remove_coffee(names_of_coffees, first_last, coffee_index)
    elif action == "Prefer":
        index1 = int(current_command[1])
        index2 = int(current_command[2])
        prefer_coffee(names_of_coffees, index1, index2)

print("Coffees:")
print(" ".join(names_of_coffees))
