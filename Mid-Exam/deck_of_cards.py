deck_of_cards = input().split(", ")
number = int(input())

for num in range(number):
    command = input().split(", ")
    action = command[0]
    if action == "Add":
        card_name = command[1]
        if card_name not in deck_of_cards:
            deck_of_cards.append(card_name)
            print("Card successfully added")
        else:
            print("Card is already in the deck")
    elif action == "Remove":
        name_of_card = command[1]
        if name_of_card in deck_of_cards:
            deck_of_cards.remove(name_of_card)
            print("Card successfully removed")
        else:
            print("Card not found")
    elif action == "Remove At":
        given_index = int(command[1])
        if 0 <= given_index < len(deck_of_cards):
            deck_of_cards.pop(given_index)
            print("Card successfully removed")
        else:
            print("Index out of range")
    elif action == "Insert":
        index1 = int(command[1])
        name_card = command[2]
        if 0 <= index1 < len(deck_of_cards):
            if name_card not in deck_of_cards:
                deck_of_cards.insert(index1, name_card)
                print("Card successfully added")
            else:
                print("Card is already added")
        else:
            print("Index out of range")

print(", ".join(deck_of_cards))
