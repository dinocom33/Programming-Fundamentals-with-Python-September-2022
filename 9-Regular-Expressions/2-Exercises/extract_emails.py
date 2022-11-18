import re

emails = input()

searches_pattern = r"\s(([a-z0-9]+[a-z0-9\.\-\_])*@[a-z\-]+(\.[a-z]+)+)\b"

result = re.findall(searches_pattern, emails)

for match in result:
    print(match[0])
