start_character = ord(input())
end_character = ord(input())
given_string = input()

result = ""
character_sum = 0

for character in given_string:
    if start_character < ord(character) < end_character:
        result += character
        character_sum += ord(character)

print(character_sum)
