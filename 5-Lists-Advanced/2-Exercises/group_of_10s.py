numbers = list(map(int, input().split(", ")))

boundary = 10

while len(numbers) > 0:
    filtered = list(filter(lambda x: x in range(boundary - 9, boundary + 1), numbers))
    numbers = [i for i in numbers if i not in filtered]
    print(f"Group of {boundary}'s: {filtered}")
    boundary += 10
