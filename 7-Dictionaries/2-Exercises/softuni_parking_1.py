def registering_car(name_of_user, plate_number):
    cars_in_parking[name_of_user] = cars_in_parking.get(name_of_user, plate_number)


def unregistering_car(user):
    del cars_in_parking[user]


number_of_commands = int(input())

cars_in_parking = {}

for command in range(number_of_commands):
    current_action = input().split()
    action, username = current_action[0], current_action[1]
    if action == "register":
        license_plate = current_action[2]
        if username in cars_in_parking:
            print(f"ERROR: already registered with plate number {license_plate}")
        else:
            registering_car(username, license_plate)
            print(f"{username} registered {license_plate} successfully")
    elif action == "unregister":
        if username not in cars_in_parking:
            print(f"ERROR: user {username} not found")
        else:
            unregistering_car(username)
            print(f"{username} unregistered successfully")

for name, number in cars_in_parking.items():
    print(f"{name} => {number}")
