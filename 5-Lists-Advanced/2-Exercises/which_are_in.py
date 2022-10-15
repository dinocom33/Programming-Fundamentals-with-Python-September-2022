first_sequence = input().split(", ")
second_sequence = input().split(", ")

final_list = []

for first_word in first_sequence:
    for second_word in second_sequence:
        if first_word in second_word:
            final_list.append(first_word)
            break

print(final_list)
