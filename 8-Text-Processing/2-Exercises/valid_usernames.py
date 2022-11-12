def check_length(word):
    if 3 <= len(word) <= 16:
        return True
    return False


def check_symbols(word):
    for character in word:
        if not (character.isalnum() or character == "-" or character == "_"):
            return False
    return True


def check_redundant_symbols(word):
    if " " in word:
        return False
    return True


def check_username(word):
    if check_length(word) and check_symbols(word) and check_redundant_symbols(word):
        return True
    return False


text = input().split(", ")

for word in text:
    if check_username(word):
        print(word)
