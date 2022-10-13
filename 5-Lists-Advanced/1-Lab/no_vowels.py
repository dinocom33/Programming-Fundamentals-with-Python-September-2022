text = input()

vowels = ['a', 'o', 'u', 'e', 'i']

final_result = ([result for result in text if result.lower() not in vowels])

# final_result = []
#
# for current_character in text:
#     if current_character.lower() not in vowels:
#         final_result.append(current_character)

print("".join(final_result))
