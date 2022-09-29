command = input()

price_wo_taxes = 0

while not (command == "special" or command == "regular"):
    current_price = float(command)
    if current_price < 0:
        print("Invalid price!")
        command = input()
        continue
    price_wo_taxes += current_price

    command = input()
taxes = price_wo_taxes * 0.20
total_price = price_wo_taxes + taxes
if command == "special":
    total_price = total_price * 0.90
if total_price == 0:
    print("Invalid order!")
else:
    print("Congratulations you've just bought a new computer!")
    print(f"Price without taxes: {price_wo_taxes:.2f}$")
    print(f"Taxes: {taxes:.2f}$")
    print("-----------")
    print(f"Total price: {total_price:.2f}$")
