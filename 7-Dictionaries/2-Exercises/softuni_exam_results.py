final_exams_result = {}
submissions = {}

while True:
    command = input()
    if command == "exam finished":
        break
    current_command = command.split("-")
    if current_command[1] == "banned":
        del final_exams_result[current_command[0]]
        continue
    username, language, points = current_command[0], current_command[1], int(current_command[2])
    if language not in submissions:
        submissions[language] = 0
    submissions[language] += 1
    if username not in final_exams_result:
        final_exams_result[username] = []
    if language not in final_exams_result[username]:
        final_exams_result[username] += language, points
    else:
        max_point = final_exams_result[username][1]
        if points > max_point:
            final_exams_result[username] = language, points

print("Results:")
for key, value in final_exams_result.items():
    print(f"{key} | {value[1]}")
print("Submissions:")
for lang, subm in submissions.items():
    print(f"{lang} - {subm}")
