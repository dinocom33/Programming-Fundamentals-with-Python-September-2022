orders_counter = int(input())

total_price = 0

for current_order in range(orders_counter):
    capsule_price = float(input())
    days = int(input())
    capsules_per_day = int(input())
    if capsule_price < 0.01 or capsule_price > 100:
        continue
    elif days < 1 or days > 31:
        continue
    elif capsules_per_day < 1 or capsules_per_day > 2000:
        continue
    price_per_order = capsule_price * days * capsules_per_day
    total_price += price_per_order
    print(f"The price for the coffee is: ${price_per_order:.2f}")
print(f"Total: ${total_price:.2f}")
