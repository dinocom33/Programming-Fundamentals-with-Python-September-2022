import math


def find_distance(x1, y1, x2, y2):
    distance = (((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5)
    return distance


x1_coordinate = float(input())
y1_coordinate = float(input())
x2_coordinate = float(input())
y2_coordinate = float(input())
x3_coordinate = float(input())
y3_coordinate = float(input())
x4_coordinate = float(input())
y4_coordinate = float(input())

x1_y1_distance = find_distance(x1_coordinate, y1_coordinate, 0, 0)
x2_y2_distance = find_distance(x2_coordinate, y2_coordinate, 0, 0)
x3_y3_distance = find_distance(x3_coordinate, y3_coordinate, 0, 0)
x4_y4_distance = find_distance(x4_coordinate, y4_coordinate, 0, 0)

first_line = x1_y1_distance + x2_y2_distance
second_line = x3_y3_distance + x4_y4_distance

if first_line >= second_line:
    if x1_y1_distance <= x2_y2_distance:
        print(f"({math.floor(x1_coordinate)}, {math.floor(y1_coordinate)})({math.floor(x2_coordinate)}, {math.floor(y2_coordinate)})")
    else:
        print(f"({math.floor(x2_coordinate)}, {math.floor(y2_coordinate)})({math.floor(x1_coordinate)}, {math.floor(y1_coordinate)})")
if second_line > first_line:
    if x3_y3_distance <= x4_y4_distance:
        print(f"({math.floor(x3_coordinate)}, {math.floor(y3_coordinate)})({math.floor(x4_coordinate)}, {math.floor(y4_coordinate)})")
    else:
        print(f"({math.floor(x4_coordinate)}, {math.floor(y4_coordinate)})({math.floor(x3_coordinate)}, {math.floor(y3_coordinate)})")
