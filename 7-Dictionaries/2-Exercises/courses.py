command = input().split(" : ")

dictionary = {}

while len(command) > 1:
    course_name, student_name = command[0], command[1]
    if course_name not in dictionary:
        dictionary[course_name] = []
    dictionary[course_name].append(student_name)

    command = input().split(" : ")

for course, value in dictionary.items():
    print(f"{course}: {len(value)}")
    for current_value in value:
        print(f"-- {current_value}")
