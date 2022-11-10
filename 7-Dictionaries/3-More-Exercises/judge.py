command = input()

judge = {}
user_points = {}

while command != "no more time":
    username, contest, points = command.split(" -> ")
    points = int(points)
    to_add_points_to_user = True
    if contest not in judge:
        judge[contest] = {username: points}
    else:
        if username not in judge[contest]:
            judge[contest][username] = points
        else:
            if points > judge[contest][username]:
                user_points[username] -= judge[contest][username]
                judge[contest].update({username: points})
            else:
                to_add_points_to_user = False
    if to_add_points_to_user:
        if username not in user_points:
            user_points[username] = 0
        user_points[username] += points
    command = input()

for key, value in judge.items():
    print(f"{key}: {len(value)} participants")
    num_counter = 1
    for current_user, point in sorted(value.items(), key=lambda x: (-x[1], x[0])):
        print(f"{num_counter}. {current_user} <::> {point}")
        num_counter += 1

print("Individual standings:")
counter = 1
for user, points in sorted(user_points.items(), key=lambda x: (-x[1], x[0])):
    print(f"{counter}. {user} -> {points}")
    counter += 1
