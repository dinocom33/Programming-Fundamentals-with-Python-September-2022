import re

text = input()

search_pattern = r"\b[A-Z][a-z]+\b \b[A-Z][a-z]+\b"

result = re.findall(search_pattern, text)

print(" ".join(result))
