legendary_items = {"shards": 0, "fragments": 0, "motes": 0}
current_items = input().split()
item_obtained = False

while not item_obtained:
    for item in range(0, len(current_items), 2):
        key = current_items[item + 1].lower()
        value = int(current_items[item])
        legendary_items[key] = legendary_items.get(key, 0)
        legendary_items[key] += value
        if legendary_items["shards"] >= 250:
            print("Shadowmourne obtained!")
            legendary_items["shards"] -= 250
            item_obtained = True
        elif legendary_items["fragments"] >= 250:
            print("Valanyr obtained!")
            legendary_items["fragments"] -= 250
            item_obtained = True
        elif legendary_items["motes"] >= 250:
            print("Dragonwrath obtained!")
            legendary_items["motes"] -= 250
            item_obtained = True
        if item_obtained:
            break
    if item_obtained:
        break
    current_items = input().split()

for key, value in legendary_items.items():
    print(f"{key}: {value}")
