number_of_students = int(input())

graded_students = {}

for current_student in range(number_of_students):
    student_name = input()
    grade = float(input())
    if student_name not in graded_students:
        graded_students[student_name] = []
    graded_students[student_name].append(float(grade))

result = {}

for student, grade in graded_students.items():
    average_grade = sum(grade) / len(grade)
    if average_grade >= 4.50:
        result[student] = average_grade

[print(f"{key} -> {result[key]:.2f}") for key in result]
