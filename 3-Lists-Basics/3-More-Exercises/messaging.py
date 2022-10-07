list_numbers = input().split(' ')
message = input()

final_message = []

for current_index in list_numbers:
    current_sum = 0
    for int_number in current_index:
        current_sum += int(int_number)
    current_sum %= len(message)
    final_message.append(message[current_sum])
    message = message.replace(message[current_sum], "", 1)

print("".join(final_message))
