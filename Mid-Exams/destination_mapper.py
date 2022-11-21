import re

places = input()

pattern = r"([=/])(?P<points>[A-Z][a-zA-Z]{2,})\1"

valid_points = re.finditer(pattern, places)
travel_points = 0
travel_map = []

for point in valid_points:
    travel_map.append(point["points"])
    travel_points += len(point["points"])
print(f"Destinations: {', '.join(travel_map)}")
print(f"Travel Points: {travel_points}")
