def odd_even_sum(number):
    even_sum = 0
    odd_sum = 0
    for n in number:
        if int(n) % 2 == 0:
            even_sum += int(n)
        else:
            odd_sum += int(n)
    return even_sum, odd_sum


current_number = input()

result = odd_even_sum(current_number)

print(f"Odd sum = {result[1]}, Even sum = {result[0]}")
