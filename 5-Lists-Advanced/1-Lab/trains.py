number_of_wagons = int(input())

wagons_in_train = [0] * number_of_wagons

while True:
    command = input()

    if command == "End":
        break

    split_command = command.split()
    action = split_command[0]
    if action == "add":
        people_to_add = int(split_command[1])
        wagons_in_train[-1] += people_to_add
    elif action == "insert":
        index = int(split_command[1])
        people_to_insert = int(split_command[2])
        wagons_in_train[index] += people_to_insert
    elif action == "leave":
        index = int(split_command[1])
        people_to_leave = int(split_command[2])
        wagons_in_train[index] -= people_to_leave

print(wagons_in_train)
