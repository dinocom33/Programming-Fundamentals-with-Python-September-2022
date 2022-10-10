import math


def find_distance(x1, y1, x2, y2):
    distance = (((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5)
    return distance


x_one = float(input())
y_one = float(input())
x_two = float(input())
y_two = float(input())

x1_y1_distance = find_distance(x_one, y_one, 0, 0)
x2_y2_distance = find_distance(x_two, y_two, 0, 0)
if x1_y1_distance <= x2_y2_distance:
    print(f"({math.floor(x_one)}, {math.floor(y_one)})")
else:
    print(f"({math.floor(x_two)}, {math.floor(y_two)})")
