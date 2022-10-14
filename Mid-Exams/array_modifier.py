def swap(list, index1, index2):
    list[index1], list[index2] = list[index2], list[index1]
    return list


initial_list = list(map(int, input().split()))
final_list = initial_list.copy()

while True:
    command = input()
    if command == "end":
        break
    current_command = command.split()
    action = current_command[0]

    if action == "swap":
        first_index = int(current_command[1])
        second_index = int(current_command[2])
        final_list[first_index], final_list[second_index] = final_list[second_index], final_list[first_index]
    elif action == "multiply":
        first_index = int(current_command[1])
        second_index = int(current_command[2])
        final_list[first_index] = final_list[first_index] * final_list[second_index]
    elif action == "decrease":
        final_list = list(map(lambda x: x - 1, final_list))

print(*final_list, sep=", ")
