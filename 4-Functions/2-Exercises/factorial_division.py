def factorials(number_a, number_b):
    factorial_a = 1
    factorial_b = 1
    for num in range(1, number_a + 1):
        factorial_a = factorial_a * num
    for num in range(1, number_b + 1):
        factorial_b = factorial_b * num
    final_result = factorial_a / factorial_b
    return final_result


first_number = int(input())
second_number = int(input())

result = factorials(first_number, second_number)
print(f"{result:.2f}")
