# Decrypting Commands
def check_index(index):
    if 0 <= index < len(initial_string):
        return True
    return False


initial_string = input()

while True:
    command = input().split()
    if command[0] == "Finish":
        break
    action = command[0]
    if action == "Replace":
        current_char, new_char = command[1], command[2]
        if current_char in initial_string:
            initial_string = initial_string.replace(current_char, new_char)
        print(initial_string)
    elif action == "Cut":
        start_index, end_index = int(command[1]), int(command[2])
        if check_index(start_index) and check_index(end_index):
            initial_string = initial_string[:start_index] + "" + initial_string[end_index + 1:]
            print(initial_string)
        else:
            print("Invalid indices!")
    elif action == "Make":
        if command[1] == "Upper":
            initial_string = initial_string.upper()
        elif command[1] == "Lower":
            initial_string = initial_string.lower()
        print(initial_string)
    elif action == "Check":
        string = command[1]
        if string in initial_string:
            print(f"Message contains {string}")
        else:
            print(f"Message doesn't contain {string}")
    elif action == "Sum":
        first_index, stop_index = int(command[1]), int(command[2])
        if check_index(first_index) and check_index(stop_index):
            temp_string = initial_string[first_index:stop_index + 1]
            char_sum = 0
            for c in temp_string:
                char_sum += ord(c)
            print(char_sum)
        else:
            print("Invalid indices!")

print()
