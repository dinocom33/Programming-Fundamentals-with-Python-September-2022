number_of_strings = int(input())

for current_string in range(1, number_of_strings + 1):
    string = input()
    if "," in string or "." in string or "_" in string:
        print(f"{string} is not pure!")
    else:
        print(f"{string} is pure.")
