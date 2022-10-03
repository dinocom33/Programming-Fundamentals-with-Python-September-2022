first_number = int(input())
second_number = int(input())

number = first_number
lst = []

for current_number in range(1, second_number + 1):
    number = first_number * current_number
    lst.append(number)

print(lst)
