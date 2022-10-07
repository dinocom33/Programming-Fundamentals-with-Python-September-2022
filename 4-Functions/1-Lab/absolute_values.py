input_string = input().split()

final_list = list()

for n in input_string:
    final_list.append(abs(float(n)))

print(final_list)
