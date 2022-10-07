times = input().split()

left_track = len(times) // 2
right_track = len(times) // 2
left_car = times[:left_track]
right_car = times[left_track + 1:]
left_car_time = 0
right_car_time = 0
winner = ""
winner_time = 0

for left_time in left_car:
    current_left_time = int(left_time)
    #    if current_left_time > 0:
    left_car_time += current_left_time
    if current_left_time == 0:
        left_car_time *= 0.8

for right_time in right_car:
    current_right_time = int(right_time)
    #    if current_right_time > 0:
    right_car_time += current_right_time
    if current_right_time == 0:
        right_car_time *= 0.8

if left_car_time < right_car_time:
    winner = "left"
    winner_time = left_car_time
else:
    winner = "right"
    winner_time = right_car_time

print(f"The winner is {winner} with total time: {winner_time:.1f}")
