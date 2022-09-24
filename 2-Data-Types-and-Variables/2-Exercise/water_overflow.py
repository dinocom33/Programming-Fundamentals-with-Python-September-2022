number_of_lines = int(input())

tank_capacity = 255
liters_in_tank = 0

for current_line in range(number_of_lines):
    litters = int(input())
    if litters > tank_capacity:
        print("Insufficient capacity!")
        continue
    liters_in_tank += litters
    tank_capacity -= litters

print(liters_in_tank)
