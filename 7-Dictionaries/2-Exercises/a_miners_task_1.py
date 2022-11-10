total_resources = {}

while True:
    resource = input()
    if resource == "stop":
        break
    quantity = int(input())
    if resource not in total_resources:
        total_resources[resource] = 0
    total_resources[resource] += quantity

for resource, quantity in total_resources.items():
    print(f"{resource} -> {quantity}")