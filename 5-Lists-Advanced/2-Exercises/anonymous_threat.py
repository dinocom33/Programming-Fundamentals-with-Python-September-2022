def merge_elements(current_list, firs_index, last_index):
    if firs_index < 0:
        firs_index = 0
    if firs_index < last_index:
        current_length = len(current_list)
        if last_index >= current_length:
            last_index = current_length - 1
        for num in range(firs_index, last_index):
            current_list[firs_index] += f"{current_list.pop(firs_index + 1)}"
    return current_list


def divide_elements(given_list, first_index, divisor):
    current_length = len(given_list[first_index])
    current_string = given_list.pop(first_index)
    divided_elements = []
    for n in range(divisor - 1):
        divided_elements.append(current_string[:current_length // divisor])
        current_string = current_string[current_length // divisor:]
    divided_elements.append(current_string)
    for e in divided_elements[::-1]:
        given_list.insert(first_index, e)
    return given_list


initial_list = input().split()

final_list = initial_list.copy()

while True:
    command = input()
    if command == "3:1":
        break
    current_command = command.split()
    action = current_command[0]
    if action == "merge":
        start_index = int(current_command[1])
        end_index = int(current_command[2])
        final_list = merge_elements(final_list, start_index, end_index)
    elif action == "divide":
        start_index = int(current_command[1])
        current_divisor = int(current_command[2])
        final_list = divide_elements(final_list, start_index, current_divisor)

print(" ".join(final_list))
