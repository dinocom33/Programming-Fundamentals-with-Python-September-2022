from math import ceil

people_count = int(input())
elevator_capacity = int(input())

courses = int(people_count / elevator_capacity)
if people_count % elevator_capacity != 0:
    courses += 1

print(courses)
