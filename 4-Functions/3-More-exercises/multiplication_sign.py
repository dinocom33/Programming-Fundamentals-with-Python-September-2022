def multiplication(number1, number2, number3):
    is_positive = True
    is_zero = False
    if number1 == 0 or number2 == 0 or number3 == 0:
        is_zero = True
    if number1 < 0 or number2 < 0 or number3 < 0:
        is_positive = False
    if (number1 < 0 and number2 < 0 and number3 > 0) or (number3 < 0 and number2 < 0 and number1 > 0) \
            or (number1 < 0 and number3 < 0 and number2 > 0):
        is_positive = True
    return is_positive, is_zero


first_number = int(input())
second_number = int(input())
third_number = int(input())

result = multiplication(first_number, second_number, third_number)

if result[1]:
    print("zero")
elif result[0]:
    print("positive")
else:
    print("negative")
