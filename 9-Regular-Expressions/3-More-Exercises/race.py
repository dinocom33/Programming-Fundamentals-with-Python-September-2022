import re

names = input().split(", ")

letter_pattern = r"[A-Za-z]+"
digits_pattern = r"\d+"
found_drivers = {}

command = input()
while command != "end of race":
    digits_found = ""
    distance = 0
    name = ""
    letter_result = re.findall(letter_pattern, command)
    digits_result = re.findall(digits_pattern, command)
    for c in letter_result:
        name += c
    if name not in found_drivers and name in names:
        found_drivers[name] = 0
    for d in digits_result:
        digits_found += d
    for digit in digits_found:
        distance += int(digit)
    if name in found_drivers:
        found_drivers[name] += distance
    command = input()

top_racers = sorted(found_drivers, key=found_drivers.get, reverse=True)[:3]

print(f"1st place: {top_racers[0]}")
print(f"2nd place: {top_racers[1]}")
print(f"3rd place: {top_racers[2]}")
