import re

text = input()

pattern = r"([#@]{1})(?P<word>[a-zA-Z]{3,})(\1{2})(?P<word2>[a-zA-Z]{3,})\1"

found_pairs = list(re.finditer(pattern, text))
valid_pairs = []

for word in found_pairs:
    if word["word"] == word["word2"][::-1]:
        valid_pairs.append(f"{word['word']} <=> {word['word2']}")

if found_pairs:
    print(f"{len(found_pairs)} word pairs found!")
    if valid_pairs:
        print("The mirror words are:")
        print(", ".join(valid_pairs))
    else:
        print("No mirror words!")
else:
    print("No word pairs found!")
    print("No mirror words!")
