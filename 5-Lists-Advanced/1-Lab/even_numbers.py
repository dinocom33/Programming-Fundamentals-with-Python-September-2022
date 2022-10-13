numbers = list(map(int, input().split(", ")))

indices = [num for num in range(len(numbers)) if numbers[num] % 2 == 0]

print(indices)
