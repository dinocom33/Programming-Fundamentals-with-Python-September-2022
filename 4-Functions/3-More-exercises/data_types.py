def find_input_type(first, second):
    result = ""
    if first == "int":
        result = int(second) * 2
    elif first == "real":
        result = f"{(float(second) * 1.5):.2f}"
    elif first == "string":
        result = f"${second}$"
    return result


first_input_string = input()
second_input_string = input()
print(find_input_type(first_input_string, second_input_string))
