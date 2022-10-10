def find_characters(character_a, character_b):
    temp_string = ""
    for char in range(ord(character_a) + 1, ord(character_b)):
        temp_string += chr(char)
    return temp_string


first_character = input()
second_character = input()

final_string = find_characters(first_character, second_character)
print(*final_string)
