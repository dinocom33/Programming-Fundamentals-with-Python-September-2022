numbers = list(map(int, input().split()))

numbers_list = numbers.copy()
average_value = sum(numbers_list) / len(numbers_list)

greater_numbers = sorted([num for num in numbers_list if num > average_value], reverse=True)

if len(greater_numbers) > 5:
    print(*greater_numbers[0:5], sep=" ")
elif len(greater_numbers) < 1:
    print("No")
else:
    print(*greater_numbers, sep=" ")
