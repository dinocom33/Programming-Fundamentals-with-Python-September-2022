import math

biscuits_per_day_per_worker = int(input())
workers_count = int(input())
other_factory_biscuits = int(input())

total_biscuits_per_month = 0

for day in range(1, 31):
    total_biscuits_per_day = int(biscuits_per_day_per_worker * workers_count)
    if day % 3 == 0:
        total_biscuits_per_day *= 0.75
    total_biscuits_per_month += int(total_biscuits_per_day)

difference = abs(total_biscuits_per_month - other_factory_biscuits)
percentage = difference / other_factory_biscuits * 100

print(f"You have produced {total_biscuits_per_month} biscuits for the past month.")

if total_biscuits_per_month > other_factory_biscuits:
    print(f"You produce {percentage:.2f} percent more biscuits.")
else:
    print(f"You produce {percentage:.2f} percent less biscuits.")
