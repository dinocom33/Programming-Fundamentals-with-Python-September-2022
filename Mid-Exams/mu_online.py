commands = input().split("|")

health = 100
bitcoins = 0
best_room = 0

for command in commands:
    current_command = command.split()
    action = current_command[0]
    value = int(current_command[1])
    best_room += 1
    if action == "potion":
        health += value
        if health > 100:
            new_value = 100 - (health - value)
            health = 100
            print(f"You healed for {new_value} hp.")
        else:
            print(f"You healed for {value} hp.")
        print(f"Current health: {health} hp.")
    elif action == "chest":
        bitcoins += value
        print(f"You found {value} bitcoins.")
    else:
        health -= value
        if health <= 0:
            print(f"You died! Killed by {action}.")
            break
        else:
            print(f"You slayed {action}.")

if health <= 0:
    print(f"Best room: {best_room}")
else:
    print("You've made it!")
    print(f"Bitcoins: {bitcoins}")
    print(f"Health: {health}")
