total_events_ingredients = input().split("|")

energy = 100
coins = 100
gained_energy = 0
is_open = True

for current_event_ingredient in total_events_ingredients:
    event_ingredient = current_event_ingredient.split("-")
    event_ingredient_type = event_ingredient[0]
    event_ingredient_value = int(event_ingredient[1])
    if event_ingredient_type == "rest":
        current_energy = energy
        energy += event_ingredient_value
        if energy > 100:
            energy = 100
        gained_energy = energy - current_energy
        print(f"You gained {gained_energy} energy.")
        print(f"Current energy: {energy}.")
    elif event_ingredient_type == "order":
        if energy >= 30:
            coins += event_ingredient_value
            energy -= 30
            print(f"You earned {event_ingredient_value} coins.")
        else:
            energy += 50
            print("You had to rest!")
    else:
        if coins >= event_ingredient_value:
            coins -= event_ingredient_value
            print(f"You bought {event_ingredient_type}.")
        else:
            is_open = False
            print(f"Closed! Cannot afford {event_ingredient_type}.")
            break

if is_open:
    print("Day completed!")
    print(f"Coins: {coins}")
    print(f"Energy: {energy}")
