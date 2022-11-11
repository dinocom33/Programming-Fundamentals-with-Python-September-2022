number_of_students = int(input())

all_students = {}

for current_student in range(number_of_students):
    student_name = input()
    grade = float(input())
    all_students[student_name] = all_students.get(student_name, [])
    all_students[student_name].append(grade)

for current_student, avg_grade in all_students.items():
    average_grade = sum(avg_grade) / len(avg_grade)
    if average_grade >= 4.50:
        print(f"{current_student} -> {average_grade:.2f}")
