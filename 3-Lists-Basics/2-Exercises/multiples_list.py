first_number = int(input())
second_number = int(input())

number = first_number
lst = []

for _ in range(second_number):
    number += first_number
    lst.append(number - first_number)

print(lst)
