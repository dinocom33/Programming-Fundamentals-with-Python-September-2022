def prepare_to_sail(command):
    targets = {}
    while command != "Sail":
        current_command = command.split("||")
        city, population, gold = current_command[0], int(current_command[1]), int(current_command[2])
        if city not in targets:
            targets[city] = [population, gold]
        else:
            targets[city][0] += population
            targets[city][1] += gold
        command = input()
    return targets


def plunder_func(targets, town, people, gold):
    targets[town][0] -= people
    targets[town][1] -= gold
    print(f"{town} plundered! {gold} gold stolen, {people} citizens killed.")
    if targets[town][0] <= 0 or targets[town][1] <= 0:
        print(f"{town} has been wiped off the map!")
        del targets[town]
    return targets


def prosper_func(targets, town, gold):
    if gold < 0:
        print("Gold added cannot be a negative number!")
    else:
        targets[town][1] += gold
        print(f"{gold} gold added to the city treasury. {town} now has {targets[town][1]} gold.")
    return targets


def print_func(targets):
    if len(targets) > 0:
        print(f"Ahoy, Captain! There are {len(targets)} wealthy settlements to go to:")
        for town, values in targets.items():
            people = values[0]
            gold = values[1]
            print(f"{town} -> Population: {people} citizens, Gold: {gold} kg")
    else:
        print(f"Ahoy, Captain! All targets have been plundered and destroyed!")


def main_func(command):
    targets = prepare_to_sail(command)
    while True:
        new_command = input()
        if new_command == "End":
            print_func(targets)
            break
        current_command = new_command.split("=>")
        action, town = current_command[0], current_command[1]
        if action == "Plunder":
            people = int(current_command[2])
            gold = int(current_command[3])
            plunder_func(targets, town, people, gold)
        elif action == "Prosper":
            gold = int(current_command[2])
            prosper_func(targets, town, gold)


command = input()
main_func(command)
