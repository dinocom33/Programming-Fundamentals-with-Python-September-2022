def piece_exists(piece):
    if piece in collection:
        return True
    return False


def add_piece(piece, composer, key, first_time: bool):
    if piece_exists(piece):
        if not first_time:
            print(f"{piece} is already in the collection!")
            return
    if not piece_exists(piece):
        collection[piece] = collection.get(piece, dict())
        collection[piece][key] = composer
        if not first_time:
            print(f"{piece} by {composer} in {key} added to the collection!")


def remove_piece(piece):
    if piece_exists(piece):
        del collection[piece]
        return f"Successfully removed {piece}!"
    return f"Invalid operation! {piece} does not exist in the collection."


def change_key(piece, new_key):
    if piece_exists(piece):
        _, composer = collection[piece].popitem()
        collection[piece] = {}
        collection[piece][key] = composer
        return f"Changed the key of {piece} to {new_key}!"
    return f"Invalid operation! {piece} does not exist in the collection."

number_of_pieces = int(input())

collection = {}

for p in range(number_of_pieces):
    piece, composer, key = input().split("|")
    add_piece(piece, composer, key, True)

while True:
    command = input()
    if command == "Stop":
        break
    current_command = command.split("|")
    current_action, current_piece = current_command[0], current_command[1]
    if current_action == "Add":
        current_composer, current_key = current_command[2], current_command[3]
        add_piece(current_piece, current_composer, current_key, False)
    elif current_action == "Remove":
        print(remove_piece(current_piece))
    elif current_action == "ChangeKey":
        new_key = current_command[2]
        print(change_key(current_piece, new_key))

for piece in collection:
    for key, composer in collection[piece].items():
        print(f"{piece} -> Composer: {composer}, Key: {key}")
