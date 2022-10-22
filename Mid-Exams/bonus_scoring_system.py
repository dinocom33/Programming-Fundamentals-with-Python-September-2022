import math

number_of_students = int(input())
number_of_lectures = int(input())
additional_bonus = int(input())

max_bonus = 0
max_attendance = 0

for student in range(1, number_of_students + 1):
    attendance = int(input())
    total_bonus = (attendance / number_of_lectures * (5 + additional_bonus))
    if total_bonus > max_bonus and attendance > max_attendance:
        max_bonus = total_bonus
        max_attendance = attendance

print(f"Max Bonus: {math.ceil(max_bonus)}.")
print(f"The student has attended {max_attendance} lectures.")
