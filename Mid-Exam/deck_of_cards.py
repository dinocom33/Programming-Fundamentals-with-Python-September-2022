def add_card(deck, card):
    if card not in deck:
        deck.append(card)
        print("Card successfully added")
    else:
        print("Card is already in the deck")


def remove_card(deck, card):
    if card in deck:
        deck.remove(card)
        print("Card successfully removed")
    else:
        print("Card not found")


def remove_at(deck, index):
    if 0 <= index < len(deck):
        deck.pop(index)
        print("Card successfully removed")
    else:
        print("Index out of range")


def insert_card(deck, index, card):
    if 0 <= index1 < len(deck_of_cards):
        if card not in deck:
            deck.insert(index, card)
            print("Card successfully added")
        else:
            print("Card is already added")
    else:
        print("Index out of range")


deck_of_cards = input().split(", ")
number = int(input())

for num in range(number):
    command = input().split(", ")
    action = command[0]
    if action == "Add":
        card_name = command[1]
        add_card(deck_of_cards, card_name)
    elif action == "Remove":
        name_of_card = command[1]
        remove_card(deck_of_cards, name_of_card)
    elif action == "Remove At":
        given_index = int(command[1])
        remove_at(deck_of_cards, given_index)
    elif action == "Insert":
        index1 = int(command[1])
        name_card = command[2]
        insert_card(deck_of_cards, index1, name_card)

print(", ".join(deck_of_cards))
