import sys

initial_list = input().split()

temp_list = []
command = input()

while command != "end":
    command_split = command.split()
    if "exchange" in command_split:
        if int(command_split[1]) > len(initial_list) or int(command_split[1]) < 0:
            print("Invalid index")
        else:
            for current_index in range(0, int(command_split[1]) + 1):
                temp_list.append(initial_list.pop(0))
            initial_list += temp_list
            temp_list = []
    elif "max" in command_split and "odd" in command_split:
        max_odd_number = -sys.maxsize
        found_odd_index = 0
        for current_index in range(len(initial_list)):
            if int(initial_list[current_index]) % 2 != 0:
                if int(initial_list[current_index]) > max_odd_number:
                    max_odd_number = int(initial_list[current_index])
                    max_odd_index = initial_list.index(initial_list[current_index])
                    found_odd_index = max_odd_index

        print(found_odd_index)
    elif "max" in command_split and "even" in command_split:
        max_even_number = -sys.maxsize
        found_even_index = 0
        for current_index in range(len(initial_list)):
            if int(initial_list[current_index]) > max_even_number:
                max_even_number = int(initial_list[current_index])
                max_even_index = initial_list.index(initial_list[current_index])
                found_even_index = max_even_index
        print(found_even_index)
#    elif found_index == 0:
#        print("No matches")

    elif "min" in command_split:
        min_odd_even_number = sys.maxsize
        found_index = 0
        for current_index in range(len(initial_list)):
            if int(initial_list[current_index]) % 2 != 0:
                if int(initial_list[current_index]) < min_odd_even_number:
                    min_odd_even_number = int(initial_list[current_index])
                    max_index = initial_list.index(initial_list[current_index])
                    found_index = max_index
            elif int(initial_list[current_index]) % 2 == 0:
                if int(initial_list[current_index]) < min_odd_even_number:
                    min_odd_even_number = int(initial_list[current_index])
                    max_index = initial_list.index(initial_list[current_index])
                    found_index = max_index
        print(found_index)
    else:
        print("No matches")



    command = input()

print('[%s]' % ', '.join(map(str, initial_list)))
