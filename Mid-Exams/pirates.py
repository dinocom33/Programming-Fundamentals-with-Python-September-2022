towns_map = {}

while True:
    add_town = input()
    if add_town == "Sail":
        break
    city, population, add_gold = add_town.split("||")
    population = int(population)
    add_gold = int(add_gold)
    towns_map[city] = towns_map.get(city, [0, 0])
    towns_map[city][0] += population
    towns_map[city][1] += add_gold

while True:
    command = input()
    if command == "End":
        break
    current_command = command.split("=>")
    action, town = current_command[0], current_command[1]
    if action == "Plunder":
        people = int(current_command[2])
        gold_stolen = int(current_command[3])
        towns_map[town][0] -= people
        towns_map[town][1] -= gold_stolen
        print(f"{town} plundered! {gold_stolen} gold stolen, {people} citizens killed.")
        if towns_map[town][0] <= 0 or towns_map[town][1] <= 0:
            del towns_map[town]
            print(f"{town} has been wiped off the map!")
    elif action == "Prosper":
        gold_to_increase = int(current_command[2])
        if gold_to_increase < 0:
            print("Gold added cannot be a negative number!")
        else:
            towns_map[town][1] += gold_to_increase
            print(f"{gold_to_increase} gold added to the city treasury. {town} now has {towns_map[town][1]} gold.")

if len(towns_map) > 0:
    print(f"Ahoy, Captain! There are {len(towns_map)} wealthy settlements to go to:")
    for town, wealthy in towns_map.items():
        print(f"{town} -> Population: {wealthy[0]} citizens, Gold: {wealthy[1]} kg")
else:
    print("Ahoy, Captain! All targets have been plundered and destroyed!")
