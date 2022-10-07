def string_to_digit(numbers):
    numbers_list = list()
    for n in numbers:
        numbers_list.append(int(n))
    return numbers_list


input_string = input().split()

print(sorted(list(string_to_digit(input_string))))
