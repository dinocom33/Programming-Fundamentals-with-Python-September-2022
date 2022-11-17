import re

text = input()
searched_string = input()

searched_pattern = fr"{searched_string}\b"

result = len(re.findall(searched_pattern.lower(), text.lower()))

print(result)
