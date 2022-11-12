def operations(number, position, operation):
    if operation == "divide":
        return number / position
    elif operation == "multiply":
        return number * position


text = input().split()

total_sum = 0

for word in text:
    number = int(word[1:len(word)-1])
    first_letter = word[0]
    last_letter = word[-1]
    if first_letter.isupper():
        first_letter_position = ord(first_letter) - 64
        total_sum += operations(number, first_letter_position, operation="divide")
    elif first_letter.islower():
        first_letter_position = ord(first_letter) - 96
        total_sum += operations(number, first_letter_position, operation="multiply")
    if last_letter.isupper():
        last_letter_position = ord(last_letter) - 64
        total_sum -= last_letter_position
    elif last_letter.islower():
        last_letter_position = ord(last_letter) - 96
        total_sum += last_letter_position

print(f"{total_sum:.2f}")
