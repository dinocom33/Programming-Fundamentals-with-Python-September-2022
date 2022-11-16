def add_plant(plant, rarity):
    all_plants[plant] = [rarity, []]


def reset_plant(plant):
    all_plants[plant][1] = []


def rate_plant(plant, rating):
    all_plants[plant][1].append(int(rating))


def update_plant(plant, rarity):
    all_plants[plant][0] = rarity


number_of_plants = int(input())

all_plants = {}

for plants in range(number_of_plants):
    new_plant, rarity = input().split("<->")
    rarity = int(rarity)
    add_plant(new_plant, rarity)

while True:
    command = input()
    if command == "Exhibition":
        break
    current_command = command.split(" - ")
    current_action = current_command[0]
    action, plant_name = current_action.split(": ")
    if action == "Reset":
        if plant_name in all_plants:
            reset_plant(plant_name)
        else:
            print("error")
    elif action == "Rate":
        new_rating = float(current_command[1])
        if plant_name in all_plants:
            rate_plant(plant_name, new_rating)
        else:
            print("error")
    elif action == "Update":
        new_rarity = int(current_command[1])
        if plant_name in all_plants:
            update_plant(plant_name, new_rarity)
        else:
            print("error")

print("Plants for the exhibition:")
for plant in all_plants:
    average_rating = 0
    if sum(all_plants[plant][1]) != 0:
        average_rating = sum(all_plants[plant][1]) / len(all_plants[plant][1])
    print(f"- {plant}; Rarity: {all_plants[plant][0]}; Rating: {average_rating:.2f}")
