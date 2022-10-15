version = list(map(int, input().split(".")))

version[-1] += 1

for number in range(len(version) - 1, -1, -1):
    if version[number] > 9:
        version[number] = 0
        if version[number - 1] >= 0:
            version[number - 1] += 1

print(*version, sep=".")
