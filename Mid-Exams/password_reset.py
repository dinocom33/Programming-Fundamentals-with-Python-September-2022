def odd_values_string(string):
    result = ""
    for i in range(len(string)):
        if i % 2 != 0:
            result = result + string[i]
    return result


initial_string = input()

command = input()

while command != "Done":
    current_command = command.split(" ")
    action = current_command[0]
    if action == "TakeOdd":
        initial_string = odd_values_string(initial_string)
        print(initial_string)
    elif action == "Cut":
        index = int(current_command[1])
        length = int(current_command[2])
#        if 0 <= index < len(initial_string) and index + length < len(initial_string):
        initial_string = initial_string[:index] + initial_string[index+length:]
        print(initial_string)
    elif action == "Substitute":
        substring = current_command[1]
        substitute = current_command[2]
        if substring in initial_string:
            initial_string = initial_string.replace(substring, substitute)
            print(initial_string)
        else:
            print("Nothing to replace!")
    command = input()

print(f"Your password is: {initial_string}")
