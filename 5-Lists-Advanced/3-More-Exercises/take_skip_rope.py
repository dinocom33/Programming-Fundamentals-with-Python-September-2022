input_string = input()

char_list = []
num_list = []
final_string = []

for current_char in input_string:
    if current_char.isnumeric():
        num_list.append(int(current_char))
    else:
        char_list.append(current_char)

for current_index in range(len(num_list)):
    if current_index % 2 == 0:
        final_string += char_list[:num_list[current_index]]
        char_list = char_list[num_list[current_index]::]
    else:
        char_list = char_list[num_list[current_index]::]


print("".join(final_string))
