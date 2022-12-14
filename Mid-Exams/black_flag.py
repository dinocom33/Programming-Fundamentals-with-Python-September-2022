days_of_plunder = int(input())
plunder_per_day = int(input())
expected_plunder = float(input())

total_plunder = 0

for day in range(1, days_of_plunder + 1):
    total_plunder += plunder_per_day
    if day % 3 == 0:
        total_plunder += plunder_per_day * 0.5
    if day % 5 == 0:
        total_plunder *= 0.7

if total_plunder >= expected_plunder:
    print(f"Ahoy! {total_plunder:.2f} plunder gained.")
else:
    percentage_left = total_plunder / expected_plunder * 100
    print(f"Collected only {percentage_left:.2f}% of the plunder.")
