command = input()

all_force_sides = {}

while command != "Lumpawaroo":
    force_user_exists = False
    if "|" in command:
        force_side, force_user = command.split(" | ")
        for user in all_force_sides.values():
            if force_user in user:
                force_user_exists = True
        if force_side not in all_force_sides:
            all_force_sides[force_side] = all_force_sides.get(force_side, [])
        if not force_user_exists:
            all_force_sides[force_side].append(force_user)
    elif " -> " in command:
        force_user, force_side = command.split(" -> ")
        for users, side in all_force_sides.items():
            if force_user in side:
                all_force_sides[users].pop(side.index(force_user))
                break
        if force_side not in all_force_sides:
            all_force_sides[force_side] = all_force_sides.get(force_side, [])
        else:
            all_force_sides[force_side].append(force_user)
        print(f"{force_user} joins the {force_side} side!")

    command = input()

for key, value in all_force_sides.items():
    if len(value) > 0:
        print(f"Side: {key}, Members: {len(value)}")
        for user in value:
            print(f"! {user}")
print()
