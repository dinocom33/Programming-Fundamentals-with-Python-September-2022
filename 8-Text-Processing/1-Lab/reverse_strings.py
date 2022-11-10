while True:
    text = input()
    if text == "end":
        break
    print(f"{text} = {text[::-1]}")
