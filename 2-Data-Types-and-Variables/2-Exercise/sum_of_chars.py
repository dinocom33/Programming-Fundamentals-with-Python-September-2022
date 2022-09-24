number_of_lines = int(input())

total_sum = 0

for current_line in range(number_of_lines):
    letter = input()
    total_sum += (ord(letter))
print(f"The sum equals: {total_sum}")
