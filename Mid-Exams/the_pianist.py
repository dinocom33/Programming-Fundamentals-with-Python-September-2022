def create_collection(number):
    collection = {}
    for _ in range(number):
        current_command = input().split("|")
        piece, composer, key = current_command[0], current_command[1], current_command[2]
        collection[piece] = [composer, key]
    return collection


def add_piece(collection, piece, composer, key):
    if piece not in collection:
        collection[piece] = [composer, key]
        print(f"{piece} by {composer} in {key} added to the collection!")
    else:
        print(f"{piece} is already in the collection!")
    return collection


def remove_piece(collection, piece):
    if piece in collection:
        del collection[piece]
        print(f"Successfully removed {piece}!")
    else:
        print(f"Invalid operation! {piece} does not exist in the collection.")
    return collection


def change_key(collection, piece, new_key):
    if piece in collection:
        collection[piece][1] = new_key
        print(f"Changed the key of {piece} to {new_key}!")
    else:
        print(f"Invalid operation! {piece} does not exist in the collection.")


def print_func(collection):
    result = ""
    for piece in collection:
        composer, key = collection[piece][0], collection[piece][1]
        result += f"{piece} -> Composer: {composer}, Key: {key}\n"
    return result


def main_function(number_of_piece):
    collection = create_collection(number_of_piece)

    while True:
        command = input()
        if command == "Stop":
            print(print_func(collection))
            break
        current_command = command.split("|")
        action, piece = current_command[0], current_command[1]
        if action == "Add":
            piece = current_command[1]
            composer = current_command[2]
            key = current_command[3]
            add_piece(collection, piece, composer, key)
        elif action == "Remove":
            remove_piece(collection, piece)
        elif action == "ChangeKey":
            new_key = current_command[2]
            change_key(collection, piece, new_key)


number_of_pieces = int(input())
main_function(number_of_pieces)
