journal = input().split(", ")

command = input()

while command != "Craft!":
    current_command = command.split(" - ")
    action = current_command[0]
    item = current_command[1]
    if action == "Collect":
        if item not in journal:
            journal.append(item)
    elif action == "Drop":
        if item in journal:
            journal.remove(item)
    elif action == "Renew":
        if item in journal:
            journal.append(journal.pop(journal.index(item)))
    elif action == "Combine Items":
        split_items = item.split(":")
        new_item = split_items[1]
        old_item = split_items[0]
        if old_item in journal:
            journal.insert(journal.index(old_item) + 1, new_item)
    command = input()

print(", ".join(journal))
