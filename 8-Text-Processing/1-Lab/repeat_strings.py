text = input().split()

# for ch in text:
#     print(ch*(len(ch)), end="")

[print(ch * len(ch), end="") for ch in text]
