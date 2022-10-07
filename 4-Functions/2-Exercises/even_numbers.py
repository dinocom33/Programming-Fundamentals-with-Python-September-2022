def find_even_numbers(numbers):
    return int(numbers) % 2 == 0


current_numbers = input().split()

filtered_list = list(filter(find_even_numbers, current_numbers))
filtered_list_as_int = list()
for n in filtered_list:
    filtered_list_as_int.append(int(n))

print(filtered_list_as_int)
