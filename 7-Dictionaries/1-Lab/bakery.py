elements = input().split(" ")

bakery = {}

for element in range(0, len(elements), 2):
    key = elements[element]
    value = elements[element + 1]
    bakery[key] = int(value)

print(bakery)
