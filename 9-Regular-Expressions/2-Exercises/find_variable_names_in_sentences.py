import re

text = input()

# search_pattern = r"(?<= _)[a-zA-Z0-9]+\b"
search_pattern = r"\b_([a-zA-Z0-9]+)\b"

result = re.findall(search_pattern, text)

print(",".join(result))
