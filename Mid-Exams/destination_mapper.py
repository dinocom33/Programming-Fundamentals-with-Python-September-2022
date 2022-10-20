import re


def substring1(string, start="=", end="="):
    final_list = []
    if start in string and end in string:
        string = string.replace(start, "**")
        string = string.split("**")
        for i in string:
            if len(i) > 0 and i.isalpha():
                if i[0].isupper() and len(i) > 3:
                    final_list.append(i)
    return final_list


def substring2(string, start="/", end="/"):
    final_list = []
    if start in string and end in string:
        string = string.replace(start, "**")
        string = string.split("**")
        for i in string:
            if len(i) > 0 and i.isalpha():
                if i[0].isupper() and len(i) > 3:
                    final_list.append(i)
    return final_list


places = input()
travel_points = 0

result = substring1(places) + substring2(places)

result_string = "".join(result)

for i in result_string:
    travel_points += 1

print(f"Destinations: {', '.join(result)}")
print(f"Travel Points: {travel_points}")
