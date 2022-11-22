import re

text = input()

emoji_pattern = r"(?P<emoji>(::|\*\*)[A-Z][a-z]{2,}\2)"
digit_pattern = r"[\d]"
cool_threshold = 1
emoji_counter = 0
emojis = {}

digit_result = re.findall(digit_pattern, text)
emoji_result = re.finditer(emoji_pattern, text)

for digit in digit_result:
    cool_threshold *= int(digit)
print(f"Cool threshold: {cool_threshold}")

for emoji in emoji_result:
    cool = 0
    current_emoji = emoji["emoji"]
    for character in current_emoji:
        if character.isalpha():
            cool += ord(character)
    emojis[current_emoji] = cool
emoji_counter = len(emojis)

print(f"{emoji_counter} emojis found in the text. The cool ones are:")
for key, value in emojis.items():
    if value >= cool_threshold:
        print(key)
