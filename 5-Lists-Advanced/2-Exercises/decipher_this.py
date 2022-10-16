def number_to_char(word: str):
    temp_word = []
    temp_char = ""
    for char in word:
        if char.isnumeric():
            temp_char += char
        else:
            temp_word.append(char)
    temp_word.insert(0, chr(int(temp_char)))
    return temp_word


def real_word(word: str):
    current_word = number_to_char(word)
    current_word[1], current_word[-1] = current_word[-1], current_word[1]
    return "".join(current_word)


message = input().split()

deciphered_message = [real_word(word) for word in message]

print(" ".join(deciphered_message))
