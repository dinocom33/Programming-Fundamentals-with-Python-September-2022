input_message = input().split(" ")

deciphered_message = []

for message in input_message:
    temp_word = []
    temp_char = ""
    for char in message:
        if char.isnumeric():
            temp_char += char
        else:
            temp_word.append(char)
    temp_word.insert(0, chr(int(temp_char)))
    temp_word[1], temp_word[-1] = temp_word[-1], temp_word[1]
    temp_list = "".join(temp_word)
    deciphered_message.append(temp_list)

print(" ".join(deciphered_message))
