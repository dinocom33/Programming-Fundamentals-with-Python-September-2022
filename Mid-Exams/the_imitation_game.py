encrypted_message = input()

command = input()

while command != "Decode":
    current_command = command.split("|")
    action = current_command[0]
    if action == "Move":
        number_of_letters = int(current_command[1])
        encrypted_message = encrypted_message[number_of_letters:] + encrypted_message[:number_of_letters]
    elif action == "Insert":
        index = int(current_command[1])
        value = current_command[2]
        if 0 <= index <= len(encrypted_message):
            encrypted_message = encrypted_message[:index] + value + encrypted_message[index:]
    elif action == "ChangeAll":
        substring = current_command[1]
        replacement = current_command[2]
        encrypted_message = encrypted_message.replace(substring, replacement)
    command = input()

print(f"The decrypted message is: {encrypted_message}")
