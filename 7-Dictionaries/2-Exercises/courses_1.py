command = input()

all_courses = {}

while command != "end":
    course_name, student_name = command.split(" : ")
    all_courses[course_name] = all_courses.get(course_name, [])
    all_courses[course_name].append(student_name)
    command = input()

for course, values in all_courses.items():
    registered_students = len(values)
    print(f"{course}: {registered_students}")
    for student in values:
        print(f"-- {student}")
