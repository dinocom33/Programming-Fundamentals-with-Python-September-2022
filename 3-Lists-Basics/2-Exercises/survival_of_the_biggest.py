list_of_numbers = input().split()
numbers_to_remove = int(input())
list_of_numbers_as_digit = []
list_of_numbers_as_digit.sort()

for current_number in list_of_numbers:
    list_of_numbers_as_digit.append(int(current_number))

for current_remove in range(numbers_to_remove):
    list_of_numbers_as_digit.remove(min(list_of_numbers_as_digit))

print(*list_of_numbers_as_digit, sep=", ")
