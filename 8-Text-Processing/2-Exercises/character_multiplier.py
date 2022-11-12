def make_sum(string_one, string_two):
    current_sum = 0
    for index in range(len(string_two)):
        current_sum += ord(string_two[index]) * ord(string_one[index])
    for index in range(len(string_two), len(string_one)):
        current_sum += ord(string_one[index])
    return current_sum


text = input()

first_string, second_string = text.split()

total_sum = 0

if len(first_string) > len(second_string):
    total_sum += make_sum(first_string, second_string)
elif len(first_string) < len(second_string):
    total_sum += make_sum(second_string, first_string)
else:
    total_sum += make_sum(first_string, second_string)

print(total_sum)
