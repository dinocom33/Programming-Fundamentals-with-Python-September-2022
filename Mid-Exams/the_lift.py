people_counter = int(input())
lift_space = input().split()

queue_is_empty = False

seats_list = []
for seats in lift_space:
    seats_list.append(int(seats))

for current_seat in range(len(seats_list)):
    while seats_list[current_seat] < 4:
        seats_list[current_seat] += 1
        people_counter -= 1
        if people_counter == 0:
            queue_is_empty = True
            break
    if queue_is_empty:
        break

if queue_is_empty and seats_list[-1] == 4:
    print(*seats_list, sep=" ")
elif queue_is_empty:
    print("The lift has empty spots!")
    print(*seats_list, sep=" ")
elif people_counter > 0:
    print(f"There isn't enough space! {people_counter} people in a queue!")
    print(*seats_list, sep=" ")
