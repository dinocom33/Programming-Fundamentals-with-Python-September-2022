fire_cells = input().split("#")
water = int(input())

water_left = water
effort = 0
total_fire = 0
print("Cells:")
for cells in fire_cells:
    current_cell = cells.split(" = ")
    if int(current_cell[1]) > water_left:
        continue
    if current_cell[0] == "High" and 80 < int(current_cell[1]) <= 125:
        water_left -= int(current_cell[1])
        total_fire += int(current_cell[1])
        effort += int(current_cell[1]) * 0.25
        print(f" - {current_cell[1]}")
    elif current_cell[0] == "Medium" and 50 < int(current_cell[1]) <= 80:
        water_left -= int(current_cell[1])
        total_fire += int(current_cell[1])
        effort += int(current_cell[1]) * 0.25
        print(f" - {current_cell[1]}")
    elif current_cell[0] == "Low" and 0 < int(current_cell[1]) <= 50:
        water_left -= int(current_cell[1])
        total_fire += int(current_cell[1])
        effort += int(current_cell[1]) * 0.25
        print(f" - {current_cell[1]}")

print(f"Effort: {effort:.2f}")
print(f"Total Fire: {total_fire}")
