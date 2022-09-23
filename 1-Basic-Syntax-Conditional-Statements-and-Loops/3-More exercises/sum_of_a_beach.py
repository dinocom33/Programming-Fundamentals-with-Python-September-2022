string = input()
lower_string = string.lower()

searched_words = ["sand", "water", "fish", "sun"]

words_count = sum([lower_string.count(word) for word in searched_words])

print(words_count)
