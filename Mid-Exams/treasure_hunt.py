def loot_items(item_list, new_items):
    for current_item in new_items:
        if current_item not in item_list:
            item_list.insert(0, current_item)
    return item_list


def drop_items(item_list, drop_index):
        item_list.append(item_list.pop(drop_index))
        return item_list


def steal_items(items_list, count_items):
    if count_items > len(items_list):
        count_items = len(items_list)
    stolen_items = []
    for current_item in range(len(items_list) - count_items, len(items_list)):
        stolen_items.append(items_list[current_item])
    print(", ".join(stolen_items))
    items_list = items_list[:len(items_list) - count_items]
    return items_list


def average_gain(items_list):
    total_gain = 0
    for current_item in items_list:
        total_gain += len(current_item)
    avg_gain = total_gain / len(initial_loot)
    return avg_gain


initial_loot = input().split("|")

command = input()

while command != "Yohoho!":
    current_command = command.split(" ")
    action = current_command[0]
    if action == "Loot":
        items_to_add = current_command[1::]
        initial_loot = loot_items(initial_loot, items_to_add)
    elif action == "Drop":
        index = int(current_command[1])
        if 0 <= index < len(initial_loot):
            initial_loot = drop_items(initial_loot, index)
    elif action == "Steal":
        count = int(current_command[1])
        initial_loot = steal_items(initial_loot, count)

    command = input()

if len(initial_loot) > 0:
    avg_gain = average_gain(initial_loot)
    print(f"Average treasure gain: {avg_gain:.2f} pirate credits.")
else:
    print("Failed treasure hunt.")
