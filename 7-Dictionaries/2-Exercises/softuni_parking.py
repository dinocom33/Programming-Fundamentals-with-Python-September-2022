number_of_cars = int(input())

dictionary = {}

for car in range(number_of_cars):
    command = input().split(" ")
    action, username = command[0], command[1]
    if action == "register":
        license_plate = command[2]
        if username not in dictionary.keys():
            dictionary[username] = license_plate
            print(f"{username} registered {license_plate} successfully")
        else:
            print(f"ERROR: already registered with plate number {license_plate}")
    elif action == "unregister":
        if username in dictionary:
            del dictionary[username]
            print(f"{username} unregistered successfully")
        else:
            print(f"ERROR: user {username} not found")

[print(f"{key} => {dictionary[key]}") for key in dictionary]

