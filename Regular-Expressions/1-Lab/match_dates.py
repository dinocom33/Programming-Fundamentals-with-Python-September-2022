import re

dates = input()

search_pattern = r"\b[a-z]+[\w.-]+@[A-Za-z0-9-]+\.[A-Z|a-z.]{2,}\b"

result = re.findall(search_pattern, dates)

for match in result:
    print(f"Day: {match[0]}, Month: {match[2]}, Year: {match[3]}")
