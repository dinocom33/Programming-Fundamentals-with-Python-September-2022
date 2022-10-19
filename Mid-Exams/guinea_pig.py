quantity_of_food_in_kg = float(input()) * 1000
quantity_of_hay_in_kg = float(input()) * 1000
quantity_of_cover_in_kg = float(input()) * 1000
pig_weight_in_kg = float(input()) * 1000

is_every_think_ok = True

for day in range(1, 31):
    quantity_of_food_in_kg -= 300
    if quantity_of_food_in_kg <= 0 or quantity_of_hay_in_kg <= 0 or quantity_of_cover_in_kg <= 0:
        is_every_think_ok = False
        break
    if day % 2 == 0:
        quantity_of_hay_in_kg -= quantity_of_food_in_kg * 0.05

    if day % 3 == 0:
        quantity_of_cover_in_kg -= pig_weight_in_kg / 3

quantity_of_food_in_kg = quantity_of_food_in_kg / 1000
quantity_of_hay_in_kg = quantity_of_hay_in_kg / 1000
quantity_of_cover_in_kg = quantity_of_cover_in_kg / 1000
if not is_every_think_ok:
    print("Merry must go to the pet store!")
else:
    print(f"Everything is fine! Puppy is happy! Food: {quantity_of_food_in_kg:.2f}, Hay: {quantity_of_hay_in_kg:.2f}, "
          f"Cover: {quantity_of_cover_in_kg:.2f}.")
