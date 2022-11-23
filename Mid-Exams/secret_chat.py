hidden_message = input()

command = input()

while command != "Reveal":
    current_command = command.split(":|:")
    action = current_command[0]
    if action == "InsertSpace":
        index = int(current_command[1])
        hidden_message = hidden_message[:index] + " " + hidden_message[index:]
        print(hidden_message)
    elif action == "Reverse":
        substring = current_command[1]
        if substring in hidden_message:
            hidden_message = hidden_message.replace(substring, "", 1)
            hidden_message += substring[::-1]
            print(hidden_message)
        else:
            print("error")
    elif action == "ChangeAll":
        substring, replacement = current_command[1], current_command[2]
        hidden_message = hidden_message.replace(substring, replacement)
        print(hidden_message)
    command = input()

print(f"You have a new text message: {hidden_message}")
