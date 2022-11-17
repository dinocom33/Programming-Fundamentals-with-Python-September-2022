import re

emails = input()

searches_pattern = re.compile(r"[a-zA-Z.-]+@[a-z-]+\.?[a-z.-]{2,}\b")

result = re.finditer(searches_pattern, emails)

for match in result:
    print(match[0])
