lost_fights_count = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())

total_price = 0

for current_game in range(1, lost_fights_count + 1):
    if current_game % 2 == 0:
        total_price += helmet_price
    if current_game % 3 == 0:
        total_price += sword_price
    if current_game % 6 == 0:
        total_price += shield_price
    if current_game % 12 == 0:
        total_price += armor_price

print(f"Gladiator expenses: {total_price:.2f} aureus")
