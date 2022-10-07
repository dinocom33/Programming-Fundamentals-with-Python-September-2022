def add_and_subtract(number_a, number_b, number_c):

    def sum_numbers():
        return number_a + number_b

    def subtract():
        return sum_numbers() - number_c

    return subtract()


first_number = int(input())
second_number = int(input())
third_number = int(input())

print(add_and_subtract(first_number, second_number, third_number))
