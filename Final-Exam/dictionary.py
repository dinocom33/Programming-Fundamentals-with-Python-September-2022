# 03. Dictionary

data = input()

test_words = []
notebook = {}

while ":" in data:
    current_data = data.split(" | ")
    for word in current_data:
        current_word, definitions = word.split(": ")
        if current_word not in notebook:
            notebook[current_word] = notebook.get(current_word, [])
        notebook[current_word].append(definitions)
    data = input()

while data != "Test" or data != "Hand Over":
    current_test_words = data.split(" | ")
    if data == "Test":
        for w in test_words:
            if w in notebook:
                print(f"{w}:")
                for value in notebook[w]:
                    print(f" -{value}")
        break
    elif data == "Hand Over":
        print(*notebook.keys(), sep=" ")
        break
    for word in current_test_words:
        test_words.append(word)
    data = input()
print()
