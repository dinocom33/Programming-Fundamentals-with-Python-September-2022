def add_plants(number):
    collection = {}
    for plants in range(number):
        plant, rarity = input().split("<->")
        if plant not in collection:
            collection[plant] = [int(rarity), []]
        else:
            collection[plant][0] += int(rarity)
    return collection


def rate_plant(collection, plant, rating):
    collection[plant][1].append(rating)
    return collection


def update_rarity(collection, plant, new_rarity):
    collection[plant][0] = new_rarity
    return collection


def reset_plant(collection, plant):
    collection[plant][1] = []
    return collection


def print_func(collection):
    result = ""
    print("Plants for the exhibition:")
    for plant, values in collection.items():
        if len(values[1]) > 0:
            average_rating = sum(values[1]) / len(values[1])
        else:
            average_rating = 0
        result += f"- {plant}; Rarity: {values[0]}; Rating: {average_rating:.2f}\n"
    return result


def main_func(number):
    collection = add_plants(number)

    while True:
        command = input()
        if command == "Exhibition":
            print(print_func(collection))
            break
        current_command = command.split(" - ")
        new_command = current_command[0].split(": ")
        action, plant = new_command[0], new_command[1]
        if action == "Rate":
            rating = int(current_command[1])
            if plant in collection:
                collection = rate_plant(collection, plant, rating)
            else:
                print("error")
        elif action == "Update":
            new_rarity = int(current_command[1])
            if plant in collection:
                collection = update_rarity(collection, plant, new_rarity)
            else:
                print("error")
        elif action == "Reset":
            if plant in collection:
                collection = reset_plant(collection, plant)
            else:
                print("error")


number_of_plants = int(input())
main_func(number_of_plants)
