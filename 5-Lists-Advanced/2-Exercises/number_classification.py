def positive_numbers(num_list):
    positive_list = [num for num in num_list if num >= 0]
    return positive_list


def negative_numbers(num_list):
    negative_list = [num for num in num_list if num < 0]
    return negative_list


def even_numbers(num_list):
    even_list = [num for num in num_list if num % 2 == 0]
    return even_list


def odd_numbers(num_list):
    odd_list = [num for num in num_list if num % 2 != 0]
    return odd_list


numbers_list = list(map(int, input().split(", ")))

print(f"Positive: {', '.join(str(num) for num in positive_numbers(numbers_list))}")
print(f"Negative: {', '.join(str(num) for num in negative_numbers(numbers_list))}")
print(f"Even: {', '.join(str(num) for num in even_numbers(numbers_list))}")
print(f"Odd: {', '.join(str(num) for num in odd_numbers(numbers_list))}")
