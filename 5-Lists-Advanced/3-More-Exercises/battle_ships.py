def moves(ships, attacks):
    destroyed_ships = 0
    for attack in attacks:
        attacked_ship = ships[attack[0]][attack[1]]
        if attacked_ship == 0:
            continue
        else:
            ships[attack[0]][attack[1]] = attacked_ship - 1
            if ships[attack[0]][attack[1]] == 0:
                destroyed_ships += 1
    return destroyed_ships


field_rows = int(input())
total_ships = []
for row in range(field_rows):
    command = list(map(int, input().split()))
    total_ships.append(command)
total_attacks = input().split()

for current_attack in range(len(total_attacks)):
    total_attacks[current_attack] = total_attacks[current_attack].split("-")
    for i in range(len(total_attacks[current_attack])):
        total_attacks[current_attack][i] = int(total_attacks[current_attack][i])

print(moves(total_ships, total_attacks))
