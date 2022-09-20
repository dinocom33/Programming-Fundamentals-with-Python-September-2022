command = input()
animals = command.replace(" ", "")
animal = animals.split(",")

sheep_count = 0
last_sheep = 0
last_animal = ""

for current_animal in animal:
    if current_animal == "sheep":
        sheep_count += 1
        last_sheep += 1
    elif current_animal == "wolf":
        last_sheep = 0
    last_animal = current_animal

if last_animal == "wolf":
    print("Please go away and stop eating my sheep")
else:
    print(f"Oi! Sheep number {last_sheep}! You are about to be eaten by a wolf!")
