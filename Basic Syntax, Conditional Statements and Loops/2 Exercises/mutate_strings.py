first_string = input()
second_string = input()

transformed_string = first_string

for current_character in range(len(first_string)):
    left_part = second_string[:current_character + 1]
    right_part = first_string[current_character + 1:]
    current_string = left_part + right_part
    if transformed_string == current_string:
        continue
    print(current_string)
    transformed_string = current_string
