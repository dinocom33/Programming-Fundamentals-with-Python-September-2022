import re

match_pattern = re.compile(r"\d+")
while True:
    numbers = input()
    if numbers:
        result = match_pattern.finditer(numbers)
        for match in result:
            print(match[0], end=" ")
    else:
        break
