import re

text = input()

search_pattern = r"(?<= _)[a-zA-Z]+\b"

result = re.findall(search_pattern, text)

print(",".join(result))
