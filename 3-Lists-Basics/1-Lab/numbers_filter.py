number_of_lines = int(input())

COMMAND_EVEN = "even"
COMMAND_ODD = "odd"
COMMAND_NEGATIVE = "negative"
COMMAND_POSITIVE = "positive"

total_numbers = []
filtered_numbers = []

for _ in range(number_of_lines):
    current_number = int(input())
    total_numbers.append(current_number)

command = input()

for number in total_numbers:
    found_number = (
        (command == COMMAND_EVEN and number % 2 == 0) or
        (command == COMMAND_ODD and number % 2 != 0) or
        (command == COMMAND_POSITIVE and number >= 0) or
        (command == COMMAND_NEGATIVE and number < 0)
    )
    if found_number:
        filtered_numbers.append(number)
print(filtered_numbers)
