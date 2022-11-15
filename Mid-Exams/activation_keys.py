activation_key = input()

while True:
    command = input()
    if command == "Generate":
        break
    current_command = command.split(">>>")
    action = current_command[0]
    if action == "Contains":
        substring = current_command[1]
        if substring in activation_key:
            print(f"{activation_key} contains {substring}")
        else:
            print(f"Substring not found!")
    elif action == "Flip":
        second_action = current_command[1]
        start_index = int(current_command[2])
        end_index = int(current_command[3])
        if second_action == "Upper":
            activation_key = activation_key[:start_index] + activation_key[
                                                                start_index:end_index].upper() + activation_key[
                                                                                                 end_index:]
            print(activation_key)
        elif second_action == "Lower":
            activation_key = activation_key[:start_index] + activation_key[
                                                            start_index:end_index].lower() + activation_key[
                                                                                             end_index:]
            print(activation_key)
    elif action == "Slice":
        start_index = int(current_command[1])
        end_index = int(current_command[2])
        activation_key = activation_key[:start_index] + activation_key[end_index:]
        print(activation_key)

print(f"Your activation key is: {activation_key}")
