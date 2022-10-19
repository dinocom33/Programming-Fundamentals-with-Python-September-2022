numbers = list(map(int, input().split(" ")))

command = input()
shots_count = 0

while command != "End":
    current_index = int(command)
    if current_index in range(len(numbers)) and numbers[current_index] != -1:
        shots_count += 1
        old_value = numbers[current_index]
        numbers[current_index] = -1
        for num in range(len(numbers)):
            if numbers[num] == -1:
                continue
            if old_value < numbers[num]:
                numbers[num] -= old_value
            else:
                numbers[num] += old_value
    command = input()
result = list(map(str, numbers))
print(f"Shot targets: {shots_count} -> {' '.join(result)}")
