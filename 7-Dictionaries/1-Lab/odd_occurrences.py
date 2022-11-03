words = input().split()

dictionary = {}

for word in words:
    if word.lower() not in dictionary:
        dictionary[word.lower()] = 0
    dictionary[word.lower()] += 1

for key, value in dictionary.items():
    if value % 2 != 0:
        print(key, end=" ")
