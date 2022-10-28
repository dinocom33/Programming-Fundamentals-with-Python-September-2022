initial_list = list(map(int, input().split(" ")))

temp_list = initial_list.copy()
even_numbers = []
odd_numbers = []

command = input()

while command != "end":
    current_command = command.split()
    action = current_command[0]
    even_numbers = [e for e in initial_list if e % 2 == 0]
    odd_numbers = [o for o in initial_list if o % 2 != 0]
    if action == "exchange":
        index = int(current_command[1])
        if 0 <= index < len(initial_list):
            left_side = initial_list[:index + 1]
            right_side = initial_list[index + 1:]
            initial_list = right_side + left_side
        else:
            print("Invalid index")

    elif action == "max":
        value = current_command[1]
        if value == "even" and even_numbers:
            print((len(initial_list) - initial_list[::-1].index(max(even_numbers)) - 1))
        elif value == "odd":
            print((len(initial_list) - initial_list[::-1].index(max(odd_numbers)) - 1))
        else:
            print("No matches")

    elif action == "min":
        value = current_command[1]
        if value == "even" and even_numbers:
            print((len(initial_list) - initial_list[::-1].index(min(even_numbers)) - 1))
        elif value == "odd":
            print((len(initial_list) - initial_list[::-1].index(min(odd_numbers)) - 1))
        else:
            print("No matches")

    elif action == "first":
        count = int(current_command[1])
        add_command = current_command[2]
        if 0 < count <= len(initial_list):
            if add_command == "even":
                print(even_numbers[0:count])
            elif add_command == "odd":
                print(odd_numbers[0:count])
        else:
            print("Invalid count")

    elif action == "last":
        count = int(current_command[1])
        add_command = current_command[2]
        if 0 < count <= len(initial_list):
            if add_command == "even":
                print(even_numbers[-count:])
            elif add_command == "odd":
                print(odd_numbers[-count:])
        else:
            print("Invalid count")

    command = input()

print(initial_list)
