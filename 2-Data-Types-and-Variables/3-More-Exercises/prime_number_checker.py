number = int(input())

is_number_prime = True

for current_number in range(2, number):
    if number % current_number == 0:
        is_number_prime = False
        break
print(is_number_prime)
