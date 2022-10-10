def sum_numbers(number_a, number_b):
    return number_a + number_b


def subtract(sum, number_c):
    return sum - number_c


def add_and_subtract(number_a, number_b, number_c):
    sum_first_second = sum_numbers(number_a, number_b)
    final_result = subtract(sum_first_second, number_c)
    return final_result


first_number = int(input())
second_number = int(input())
third_number = int(input())

print(add_and_subtract(first_number, second_number, third_number))
