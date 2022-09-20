divisor = int(input())
boundary = int(input())

number_found = 0

for largest_int in range(1, boundary + 1):
    if largest_int % divisor == 0 and largest_int > number_found:
        number_found = largest_int
print(number_found)
