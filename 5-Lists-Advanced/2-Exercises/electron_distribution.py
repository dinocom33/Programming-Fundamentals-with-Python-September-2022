number_of_electrons = int(input())

final_list = []
n = 1


for num in range(1, number_of_electrons + 1):
    if sum(final_list) == number_of_electrons:
        break
    if sum(final_list) + (2 * n**2) > number_of_electrons:
        final_list.append(abs(sum(final_list) - number_of_electrons))
        break
    final_list.append(2 * n**2)
    n += 1

print(final_list)
