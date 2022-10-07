input_string = input().split()

final_list = list()

for current_string in input_string:
    final_list.append(round(float(current_string)))

print(final_list)
