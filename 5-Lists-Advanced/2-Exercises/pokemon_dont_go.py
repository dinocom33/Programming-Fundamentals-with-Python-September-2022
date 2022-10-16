distance = list(map(int, input().split()))

sum_of_removed_numbers = 0

for current_number in distance:
    while len(distance) != 0:
        current_index = int(input())
        removed_number = 0
        if 0 <= current_index < len(distance):
            removed_number = distance.pop(current_index)
        elif current_index < 0:
            removed_number = distance[0]
            distance[0] = distance[-1]
        else:
            removed_number = distance[-1]
            distance[-1] = distance[0]
        sum_of_removed_numbers += removed_number

        for index, number in enumerate(distance):
            if number <= removed_number:
                distance[index] += removed_number
            else:
                distance[index] -= removed_number

print(sum_of_removed_numbers)
