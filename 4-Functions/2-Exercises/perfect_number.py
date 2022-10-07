def perfect_number(number):
    divisors = list()
    for num in range(1, number):
        if number % num == 0:
            divisors.append(num)
    return divisors


input_number = int(input())

if sum(perfect_number(input_number)) == input_number:
    print("We have a perfect number!")
else:
    print("It's not so perfect.")
