initial_string = list(map(int, input().split("@")))

jumps_counter = 0
last_visited_house = 0
house_wo_valentine = 0

command = input()

while command != "Love!":
    current_command = command.split(" ")
    jump = current_command[0]
    jump_step = int(current_command[1])
    jumps_counter += 1

    if jumps_counter > 1:
        jump_step += last_visited_house
    if jump_step >= len(initial_string):
        jumps_counter = 0
        jump_step = 0

    last_visited_house = jump_step

    if initial_string[jump_step] == 0:
        print(f"Place {jump_step} already had Valentine's day.")

    initial_string[jump_step] -= 2
    if initial_string[jump_step] == 0:
        print(f"Place {jump_step} has Valentine's day.")

    command = input()

print(f"Cupid's last position was {last_visited_house}.")

for house in initial_string:
    if house > 0:
        house_wo_valentine += 1

if house_wo_valentine == 0:
    print(f"Mission was successful.")
else:
    print(f"Cupid has failed {house_wo_valentine} places.")
