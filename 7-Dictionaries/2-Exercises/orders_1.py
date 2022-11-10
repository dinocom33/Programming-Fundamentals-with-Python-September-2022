all_products = {}

while True:
    command = input().split()
    if "buy" in command:
        break
    product, price, quantity = command[0], float(command[1]), int(command[2])
    all_products[product] = all_products.get(product, [0, 0])
    all_products[product][0] = price
    all_products[product][1] += quantity

for name, values in all_products.items():
    total_price = values[0] * values[1]
    print(f"{name} -> {total_price:.2f}")
