key = int(input())
number_of_lines = int(input())

message = ""

for current_line in range(1, number_of_lines + 1):
    letter = input()
    message += chr(ord(letter) + key)
print(message)
