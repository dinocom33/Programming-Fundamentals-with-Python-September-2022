names_of_coffees = input().split(" ")
count_commands = int(input())

for command in range(count_commands):
    current_command = input().split(" ")
    action = current_command[0]
    if action == "Reverse":
        names_of_coffees.reverse()
    elif action == "Include":
        coffee_to_include = current_command[1]
        names_of_coffees.append(coffee_to_include)
    elif action == "Remove":
        first_last = current_command[1]
        coffee_index = int(current_command[2])
        if coffee_index < len(names_of_coffees):
            if first_last == "first":
                names_of_coffees = names_of_coffees[coffee_index:]
            elif first_last == "last":
                names_of_coffees = names_of_coffees[:-coffee_index]
    elif action == "Prefer":
        index1 = int(current_command[1])
        index2 = int(current_command[2])
        if index1 < len(names_of_coffees) and index2 < len(names_of_coffees):
            names_of_coffees[index1], names_of_coffees[index2] = names_of_coffees[index2], names_of_coffees[index1]

print("Coffees:")
print(" ".join(names_of_coffees))
