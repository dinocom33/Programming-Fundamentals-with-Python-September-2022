people_list = input().split()
number = int(input())
kills_counter = 0
current_people_list_index = 0
final_list = []

# Start loop until length of string is > 0
while len(people_list) > 0:
    kills_counter += 1
    # Check if the counter is equal to the number and if it is - kill the person sitting on that index. Remove it from
    #   people_list and append it to final_list.
    if kills_counter % number == 0:
        final_list.append(people_list.pop(current_people_list_index))
    else:
        current_people_list_index += 1
    # If current index is out of length of the list reset it to 0.
    if current_people_list_index >= len(people_list):
        current_people_list_index = 0
# Format final_list according to the condition.
final_list = str(final_list).replace(" ", "").replace("'", "")
print(final_list, sep=",")
