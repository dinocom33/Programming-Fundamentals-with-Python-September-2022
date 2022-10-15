number_of_rooms = int(input())

needed_chairs = 0
free_chairs = 0

for room in range(1, number_of_rooms + 1):
    command = input().split()
    chairs = command[0]
    visitors = int(command[1])
    difference = abs(len(chairs) - visitors)
    if len(chairs) < visitors:
        print(f"{difference} more chairs needed in room {room}")
        needed_chairs += difference
    else:
        free_chairs += difference

if free_chairs >= needed_chairs:
    print(f"Game On, {free_chairs} free chairs left")
