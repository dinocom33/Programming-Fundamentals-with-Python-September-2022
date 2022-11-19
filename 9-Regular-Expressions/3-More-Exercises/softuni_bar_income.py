import re

pattern = r"%([A-Z][a-z]+)%[a-zA-Z0-9]*<([\w\d]+)>[a-zA-Z0-9]*\|(\d+)\|[a-zA-Z]*(\d+\.?\d+?)\$"

command = input()
total_income = 0

while command != "end of shift":
    search_result = re.findall(pattern, command)
    total_price = 0
    if search_result:
        name = search_result[0][0]
        product = search_result[0][1]
        quantity = int(search_result[0][2])
        price = float(search_result[0][3])
        total_price += quantity * price
        total_income += total_price
        print(f"{name}: {product} - {total_price:.2f}")
    command = input()

print(f"Total income: {total_income:.2f}")
