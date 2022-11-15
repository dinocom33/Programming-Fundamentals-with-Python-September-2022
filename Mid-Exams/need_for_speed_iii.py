def add_car(car, mileage, fuel):
    all_cars[car] = all_cars.get(car, [0, 0])
    all_cars[car][0] += mileage
    all_cars[car][1] += fuel


def drive(car, distance, fuel):
    if fuel <= all_cars[car][1]:
        all_cars[car][0] += distance
        all_cars[car][1] -= fuel
        return f"{car} driven for {distance} kilometers. {fuel} liters of fuel consumed."
    return f"Not enough fuel to make that ride"


def refuel(car, fuel):
    if all_cars[car][1] + fuel > max_fuel:
        fuel = max_fuel - all_cars[car][1]
    all_cars[car][1] += fuel
    return f"{car} refueled with {fuel} liters"


def revert(car, kilometers):
    if (all_cars[car][0] - kilometers) < 10000:
        all_cars[car][0] = 10000
    else:
        all_cars[car][0] -= kilometers
        return f"{car} mileage decreased by {kilometers} kilometers"


number_of_cars = int(input())

all_cars = {}
max_fuel = 75

for cars in range(number_of_cars):
    first_command = input().split("|")
    new_car, new_mileage, new_fuel = first_command[0], int(first_command[1]), int(first_command[2])
    add_car(new_car, new_mileage, new_fuel)

while True:
    command = input()
    if command == "Stop":
        break
    current_command = command.split(" : ")
    action, current_car = current_command[0], current_command[1]
    if action == "Drive":
        car_distance = int(current_command[2])
        car_fuel = int(current_command[3])
        print(drive(current_car, car_distance, car_fuel))
        if all_cars[current_car][0] >= 100000:
            del all_cars[current_car]
            print(f"Time to sell the {current_car}!")
    elif action == "Refuel":
        add_fuel = int(current_command[2])
        print(refuel(current_car, add_fuel))
    elif action == "Revert":
        kilometers_to_decrease = int(current_command[2])
        print(revert(current_car, kilometers_to_decrease))

for car, value in all_cars.items():
    mileage = value[0]
    fuel = value[1]
    print(f"{car} -> Mileage: {mileage} kms, Fuel in the tank: {fuel} lt.")
