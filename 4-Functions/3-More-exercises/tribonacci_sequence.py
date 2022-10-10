def tribonacci(current_number):
    initial_list = [1, 0, 0]
    tribonacci_list = []
    for current_number in range(number):
        next_number = sum(initial_list)
        tribonacci_list.append(next_number)
        initial_list.append(next_number)
        initial_list.pop(0)
    return tribonacci_list


number = int(input())
final_list = tribonacci(number)
print(*final_list, sep=" ")
