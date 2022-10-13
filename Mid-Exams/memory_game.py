def index_in_list(elements, index):
    if 0 <= int(index) < len(elements):
        return True
    else:
        return False


sequence_of_elements = input().split()
command = input()

moves_counter = 0

while command != "end":
    current_integers = command.split()
    first_index = int(current_integers[0])
    second_index = int(current_integers[1])
    if len(sequence_of_elements) < 2:
        break
    moves_counter += 1
    if index_in_list(sequence_of_elements, first_index) and index_in_list(sequence_of_elements, second_index) \
            and first_index != second_index:
        if sequence_of_elements[first_index] == sequence_of_elements[second_index]:
            print(f"Congrats! You have found matching elements - {sequence_of_elements[first_index]}!")
            if second_index > 0:
                second_index -= 1
            sequence_of_elements.pop(first_index)
            sequence_of_elements.pop(second_index)
        elif sequence_of_elements[first_index] != sequence_of_elements[second_index]:
            print("Try again!")
    else:
        middle_of_sequence_of_element = len(sequence_of_elements) // 2
        sequence_of_elements.insert(middle_of_sequence_of_element, f"-{moves_counter}a")
        sequence_of_elements.insert(middle_of_sequence_of_element, f"-{moves_counter}a")
        print("Invalid input! Adding additional elements to the board")

    command = input()

if len(sequence_of_elements) < 2:
    print(f"You have won in {moves_counter} turns!")
else:
    print("Sorry you lose :(")
    print(*sequence_of_elements, sep=" ")
