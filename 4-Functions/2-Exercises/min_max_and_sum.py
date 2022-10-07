def min_max_sum(numbers):
    numbers_list = list()
    for n in numbers:
        numbers_list.append(int(n))
    min_number = min(numbers_list)
    max_number = max(numbers_list)
    sum_of_numbers = sum(numbers_list)
    return min_number, max_number, sum_of_numbers


input_numbers = input().split()

result = min_max_sum(input_numbers)

print(f"The minimum number is {result[0]}")
print(f"The maximum number is {result[1]}")
print(f"The sum number is: {result[2]}")
