import re

text = input()

searched_pattern = r"([#\|])([A-Za-z ]+)\1(?P<date>[0-9]{2}/[0-9]{2}/[0-9]{2})\1(?P<calories>\d+)\1"

result = re.finditer(searched_pattern, text)

final_result = {}
total_calories = 0

for match in result:
    item = match[2]
    date = match[3]
    calories = int(match[4])
    total_calories += calories
    final_result[item] = final_result.get(item, list())
    final_result[item].append(date)
    final_result[item].append(calories)

days = total_calories // 2000
print(f"You have food to last you for: {days} days!")
for key, value in final_result.items():
    print(f"Item: {key}, Best before: {value[0]}, Nutrition: {value[1]}")
