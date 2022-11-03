characters = input().split(", ")

result = {}

for element in characters:
    key, value = element, ord(element)
    result[key] = value

print(result)
