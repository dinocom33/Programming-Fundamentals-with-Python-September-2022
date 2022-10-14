receptionists = [int(input()) for num in range(3)]
students = int(input())
all_receptionists = sum(receptionists)
hours_count = 0
students_left = students

while students_left > 0:
    hours_count += 1
    if hours_count > 0 and hours_count % 4 == 0:
        continue
    students_left -= all_receptionists

print(f"Time needed: {hours_count}h.")
