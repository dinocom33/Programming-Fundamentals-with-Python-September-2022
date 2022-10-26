pirate_ship_status = list(map(int, input().split(">")))
warship_status = list(map(int, input().split(">")))
max_health = int(input())

pirate_ship_sunk = False
warship_sunk = False

command = input()

while command != "Retire":
    current_command = command.split(" ")
    action = current_command[0]
    if action == "Status":
        section_for_repair = 0
        for section in range(len(pirate_ship_status)):
            if pirate_ship_status[section] < max_health * 0.2:
                section_for_repair += 1
        if section_for_repair > 0:
            print(f"{section_for_repair} sections need repair.")
    elif action == "Fire":
        index_to_fire = int(current_command[1])
        damage = int(current_command[2])
        if 0 <= index_to_fire < len(warship_status):
            warship_status[index_to_fire] -= damage
            if warship_status[index_to_fire] <= 0:
                warship_sunk = True
        if warship_sunk:
            print("You won! The enemy ship has sunken.")
            break
    elif action == "Repair":
        index_to_repair = int(current_command[1])
        health = int(current_command[2])
        if 0 <= index_to_repair < len(pirate_ship_status):
            pirate_ship_status[index_to_repair] += health
            if pirate_ship_status[index_to_repair] > max_health:
                pirate_ship_status[index_to_repair] = max_health
    elif action == "Defend":
        start_index = int(current_command[1])
        end_index = int(current_command[2])
        defend_damage = int(current_command[3])
        if 0 <= start_index < len(pirate_ship_status) and 0 <= end_index < len(pirate_ship_status):
            for section in range(start_index, end_index + 1):
                pirate_ship_status[section] -= defend_damage
                if pirate_ship_status[section] <= 0:
                    pirate_ship_sunk = True
        if pirate_ship_sunk:
            print("You lost! The pirate ship has sunken.")
            break
    command = input()

if command == "Retire":
    print(f"Pirate ship status: {sum(pirate_ship_status)}")
    print(f"Warship status: {sum(warship_status)}")
