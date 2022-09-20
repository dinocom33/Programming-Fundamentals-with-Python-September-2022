budget = float(input())
flour_per_kg = float(input())

eggs_price_per_pack = flour_per_kg * 0.75
milk_price_per_lt = (flour_per_kg * 1.25) / 4

eggs_counter = 0
bred_counter = 0
money_left = budget
bread_price = flour_per_kg + eggs_price_per_pack + milk_price_per_lt

while money_left >= bread_price:
    bred_counter += 1
    eggs_counter += 3
    money_left -= bread_price
    if bred_counter % 3 == 0:
        eggs_counter -= (bred_counter - 2)

print(f"You made {bred_counter} loaves of Easter bread! Now you have {eggs_counter} eggs and {money_left:.2f}BGN left.")
