def message_encryption(message):
    new_message = ""
    for character in message:
        new_message += chr(ord(character) + 3)
    return new_message


text = input()

encrypted_text = message_encryption(text)

print(encrypted_text)
