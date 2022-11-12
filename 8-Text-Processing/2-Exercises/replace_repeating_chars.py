def remove_repeating_chars(string):
    temp_string = ""
    last_letter = ""
    for char in string:
        if char != last_letter:
            temp_string += char
            last_letter = char
    return temp_string


some_string = input()

final_string = remove_repeating_chars(some_string)

print(final_string)
