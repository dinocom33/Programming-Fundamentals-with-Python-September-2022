number_of_cars = int(input())

parking_places = {}

for car in range(number_of_cars):
    command = input().split(" ")
    action, username = command[0], command[1]
    if action == "register":
        license_plate = command[2]
        if username not in parking_places.keys():
            parking_places[username] = license_plate
            print(f"{username} registered {license_plate} successfully")
        else:
            print(f"ERROR: already registered with plate number {license_plate}")
    elif action == "unregister":
        if username in parking_places:
            del parking_places[username]
            print(f"{username} unregistered successfully")
        else:
            print(f"ERROR: user {username} not found")

for username, car in parking_places.items():
    print(f"{username} => {car}")
#[print(f"{key} => {parking_places[key]}") for key in parking_places]
