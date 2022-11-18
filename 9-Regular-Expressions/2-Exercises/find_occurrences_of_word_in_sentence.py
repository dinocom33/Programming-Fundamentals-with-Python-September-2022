import re

text = input()
searched_string = input()

searched_pattern = fr"\b{searched_string}\b"

result = re.findall(searched_pattern, text, flags=re.I)

print(len(result))
