command = input()

dictionary = {}

while command != "buy":
    current_command = command.split(" ")
    product, price, quantity = current_command[0], float(current_command[1]), int(current_command[2])
    command = input()
    if product not in dictionary.keys():
        dictionary[product] = []
        dictionary[product].append(price)
        dictionary[product].append(quantity)
    else:
        dictionary[product][0] = price
        dictionary[product][1] += quantity

for product in dictionary:
    total_price = dictionary[product][0] * dictionary[product][1]
    print(f"{product} -> {total_price:.2f}")
