import re

command = input()
pattern = r">>([A-Za-z]+)<<(\d+\.?\d*)!(\d+)"
all_furniture = []
total_sum = 0

while command != "Purchase":
    result = re.findall(pattern, command)
    if result:
        furniture = result[0][0]
        price = float(result[0][1])
        quantity = int(result[0][2])
        all_furniture.append(furniture)
        total_sum += price * quantity
    command = input()

print("Bought furniture:")
for item in all_furniture:
    print(item)
print(f"Total money spend: {total_sum:.2f}")
