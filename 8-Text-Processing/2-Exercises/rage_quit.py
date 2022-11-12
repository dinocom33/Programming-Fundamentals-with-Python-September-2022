some_string = input()

final_string = ""
temp_string = ""
number = ""

for index, symbol in enumerate(some_string):
    last_symbol = ""
    if not symbol.isdigit():
        temp_string += symbol
    elif symbol.isdigit:
        number += symbol
        if index + 1 < len(some_string):
            if some_string[index + 1].isdigit():
                continue
        final_string += temp_string * int(number)
        temp_string = ""
        number = ""

final_string = final_string.upper()
print(f"Unique symbols used: {len(set(final_string))}")
print(final_string)
