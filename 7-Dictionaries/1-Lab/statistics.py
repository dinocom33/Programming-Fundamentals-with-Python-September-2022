command = input()

products = {}

while command != "statistics":
    key, value = command.split(":")
    if key not in products:
        products[key] = 0
    products[key] += int(value)
    command = input()

print("Products in stock:")
for key, value in products.items():
    print(f"- {key}: {value}")
print(f"Total Products: {len(products)}")
print(f"Total Quantity: {sum(products.values())}")
