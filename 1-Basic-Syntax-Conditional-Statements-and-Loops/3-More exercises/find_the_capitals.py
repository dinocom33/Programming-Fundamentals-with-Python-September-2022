command = input()

result = []

for i in range(0, len(command)):
    if ord(command[i]) in range(65, 91):
        result.append(i)
print(result)
