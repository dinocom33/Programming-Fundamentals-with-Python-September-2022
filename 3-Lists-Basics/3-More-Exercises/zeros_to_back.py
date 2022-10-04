numbers = input().split(", ")

new_number_lst = []
zero_counter = 0

for number in numbers:
    current_number = int(number)
    if current_number != 0:
        new_number_lst.append(current_number)
    else:
        zero_counter += 1
for zero in range(zero_counter):
    new_number_lst.append(0)

print(new_number_lst)
