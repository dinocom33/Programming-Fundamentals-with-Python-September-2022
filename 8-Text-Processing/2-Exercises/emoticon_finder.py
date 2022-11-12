def emoticon_finder(string):
    emoticons = []
    for index in range(len(string)):
        if string[index] == ":":
            emoticons.append(f"{string[index]}{string[index + 1]}")
    return emoticons


text = input()

emoticon = emoticon_finder(text)

print(*emoticon, sep='\n')
