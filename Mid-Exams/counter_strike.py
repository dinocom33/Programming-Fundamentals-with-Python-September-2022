initial_energy = int(input())

command = input()
energy_left = initial_energy
wins_count = 0

while command != "End of battle":
    current_command = int(command)

    if wins_count % 3 == 0:
        energy_left += wins_count

    if energy_left < current_command:
        print(f"Not enough energy! Game ends with {wins_count} won battles and {energy_left} energy")
        break
    energy_left -= current_command
    wins_count += 1
    command = input()

if command == "End of battle":
    print(f"Won battles: {wins_count}. Energy left: {energy_left}")
