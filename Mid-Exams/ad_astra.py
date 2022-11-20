import re

text = input()

searched_pattern = r"([#|])(?P<item>[A-Za-z ]+)\1(?P<date>[0-9]{2}/[0-9]{2}/[0-9]{2})\1(?P<calories>[0-9]{1,5})\1"

result = re.finditer(searched_pattern, text)

final_result = []
total_calories = 0

for match in result:
    item, date, calories = match["item"], match["date"], int(match["calories"])
    total_calories += calories
    final_result.append({"name": item, "date": date, "calories": calories})
    # final_result[item].append(date)
    # final_result[item].append(calories)

days = total_calories // 2000
print(f"You have food to last you for: {days} days!")
for current_item in final_result:
    print(f"Item: {current_item['name']}, Best before: {current_item['date']}, Nutrition: {current_item['calories']}")
