import re

all_points = input()

pattern = r"([=|\/])(?P<point>[A-Z][a-zA-Z]{2,})\1"
final_points = []
travel_points = 0
result = re.finditer(pattern, all_points)

for point in result:
    final_points.append(point.group("point"))
    travel_points += len(point.group("point"))

print(f"Destinations: {', '.join(final_points)}")
print(f"Travel Points: {travel_points}")
