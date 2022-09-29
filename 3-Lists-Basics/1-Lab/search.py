number = int(input())
filter_word = input()

total_lst = []
filtered_lst = []

for _ in range(number):
    current_string = input()
    total_lst.append(current_string)
    if filter_word in current_string:
        filtered_lst.append(current_string)

print(total_lst)
print(filtered_lst)
