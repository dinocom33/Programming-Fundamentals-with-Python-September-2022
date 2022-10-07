def find_smallest_number(first_number, second_number, third_number):
    number_list = list()
    number_list.append(first_number)
    number_list.append(second_number)
    number_list.append(third_number)
    return min(number_list)


first_number = int(input())
second_number = int(input())
third_number = int(input())

print(find_smallest_number(first_number, second_number, third_number))
