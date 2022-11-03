words_count = int(input())

dictionary = {}

for current_word in range(words_count):
    word = input()
    synonym = input()
    if word not in dictionary.keys():
        dictionary[word] = []
    dictionary[word].append(synonym)

# for synonym in dictionary:
#    print(f"{synonym} - {', '.join(dictionary[synonym])}")

[print(f"{synonym} - {', '.join(dictionary[synonym])}") for (synonym) in dictionary]
