number = int(input())

for num in range(number):
    line = input().split()
    name = ""
    age = ""
    for value in line:
        if "@" in value and "|" in value:
            name += value[value.index("@") + 1:value.index("|")]
        if "#" in value and "*" in value:
            age += value[value.index("#") + 1:value.index("*")]
    print(f"{name} is {age} years old.")
