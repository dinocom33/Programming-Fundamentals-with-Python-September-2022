goods_for_beggars = input().split(", ")
number_of_beggars = int(input())

goods_for_beggars_as_digit = []
total_goods = []
starting_index = 0

for current_digit in goods_for_beggars:
    goods_for_beggars_as_digit.append(int(current_digit))

while starting_index < number_of_beggars:
    current_goods = 0
    for current_index in range(starting_index, len(goods_for_beggars_as_digit), number_of_beggars):
        current_goods += goods_for_beggars_as_digit[current_index]
    total_goods.append(current_goods)
    starting_index += 1

print(total_goods)
