dictionary = {}
legendary_item_found = False

while not legendary_item_found:
    items = input().split()
    for i in range(0, len(items), 2):
        value, key = items[i], items[i + 1]
        key_lower = key.lower()
        if key_lower not in dictionary:
            dictionary[key_lower] = 0
        dictionary[key_lower] += int(value)
        if key_lower == "motes" and dictionary[key_lower] >= 250:
            legendary_item_found = True
            print("Dragonwrath obtained!")
            break
        elif key_lower == "shards" and dictionary[key_lower] >= 250:
            legendary_item_found = True
            print("Shadowmourne obtained!")
            break
        elif key_lower == "fragments" and dictionary[key_lower] >= 250:
            legendary_item_found = True
            print("Valanyr obtained!")
            break

print()
