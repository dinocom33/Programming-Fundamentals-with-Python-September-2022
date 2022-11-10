contests = {}
submissions = {}
max_points = 0
best_user = ""

while True:
    command = input()
    if command == "end of contests":
        break
    contest1, password1 = command.split(":")
    if contest1 not in contests:
        contests[contest1] = password1

while True:
    second_command = input()
    if second_command == "end of submissions":
        break
    contest, password, username, points = second_command.split("=>")
    points = int(points)
    if contest in contests and password == contests[contest]:
        if username not in submissions.keys():
            submissions[username] = {contest: points}
        else:
            if contest in submissions[username]:
                if points > submissions[username][contest]:
                    submissions[username].update({contest: points})
            else:
                submissions[username].update({contest: points})

for user, value in submissions.items():
    current_max_points = 0
    for contest, current_points in value.items():
        current_max_points += current_points
    if current_max_points > max_points:
        max_points = current_max_points
        best_user = user

print(f"Best candidate is {best_user} with total {max_points} points.")
print("Ranking:")
sorted_submissions = {key: value for key, value in sorted(submissions.items())}
for username, value in sorted_submissions.items():
    print(username)
    for contest, points in sorted(value.items(), key=lambda x: -x[1]):
        print(f"#  {contest} -> {points}")
