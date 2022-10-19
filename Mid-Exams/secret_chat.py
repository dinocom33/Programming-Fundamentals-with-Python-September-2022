hidden_message = input()

command = input()

while command != "Reveal":
    current_command = command.split(":|:")
    action = current_command[0]
    if action == "InsertSpace":
        index = int(current_command[1])
        hidden_message = "".join((hidden_message[:index], " ", hidden_message[index:]))
        print(hidden_message)
    elif action == "Reverse":
        substring = current_command[1]
        if substring in hidden_message:
            hidden_message = hidden_message.replace(substring, "", 1)
            substring = "".join(reversed(substring))
            hidden_message += substring
            print(hidden_message)
        else:
            print("error")
    elif action == "ChangeAll":
        substring = current_command[1]
        replacement = current_command[2]
        for char in hidden_message:
            if char == substring:
                hidden_message = hidden_message.replace(char, replacement)
        print(hidden_message)
    command = input()

print(f"You have a new text message: {hidden_message}")
