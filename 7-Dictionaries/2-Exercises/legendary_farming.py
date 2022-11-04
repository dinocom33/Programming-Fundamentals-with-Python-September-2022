dictionary = {"shards": 0, "fragments": 0, "motes": 0}
items = input().split()
legendary_item_found = False

while not legendary_item_found:
    for i in range(0, len(items), 2):
        value, key = int(items[i]), items[i + 1].lower()
        if key not in dictionary:
            dictionary[key] = 0
        dictionary[key] += value
        if key == "motes" and dictionary[key] >= 250:
            dictionary[key] -= 250
            legendary_item_found = True
            print("Dragonwrath obtained!")
        elif key == "shards" and dictionary[key] >= 250:
            dictionary[key] -= 250
            legendary_item_found = True
            print("Shadowmourne obtained!")
        elif key == "fragments" and dictionary[key] >= 250:
            dictionary[key] -= 250
            legendary_item_found = True
            print("Valanyr obtained!")
        if legendary_item_found:
            break
    if legendary_item_found:
        break
    items = input().split()

for key, item in dictionary.items():
    print(f"{key}: {item}")
