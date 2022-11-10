final_force_users = {}

while True:
    command = input()
    if command == "Lumpawaroo":
        break
    if "|" in command:
        current_command = command.split(" | ")
        force_side, force_user = current_command[0], current_command[1]
        user_is_in_force = False
        for value in final_force_users.values():
            if force_user in value:
                user_is_in_force = True
        if force_side not in final_force_users:
            final_force_users[force_side] = []
        if not user_is_in_force:
            final_force_users[force_side].append(force_user)
    elif " -> " in command:
        current_command = command.split(" -> ")
        force_user, force_side = current_command[0], current_command[1]
        for user, side in final_force_users.items():
            if force_user in side:
                final_force_users[user].pop(side.index(force_user))
                break
        if force_side not in final_force_users:
            final_force_users[force_side] = [force_user]
        else:
            final_force_users[force_side].append(force_user)
        print(f"{force_user} joins the {force_side} side!")

for side, users in final_force_users.items():
    if len(users) > 0:
        print(f"Side: {side}, Members: {len(users)}")
        for user in users:
            print(f"! {user}")
