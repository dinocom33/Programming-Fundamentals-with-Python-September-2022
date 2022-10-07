first_row = input().split()
second_row = input().split()
third_row = input().split()

player_number = 1
player_name = ""
is_player_one_win = False
is_player_two_win = False

while player_number < 3:
    player_number = str(player_number)
    wining_combination = [player_number, player_number, player_number]
    if first_row == wining_combination or second_row == wining_combination or third_row == wining_combination:
        if player_number == "1":
            is_player_one_win = True
        else:
            is_player_two_win = True
    for current_column in range(len(first_row)):
        if first_row[current_column] == player_number and second_row[current_column] == player_number and \
                third_row[current_column] == player_number:
            if player_number == "1":
                is_player_one_win = True
            else:
                is_player_two_win = True
    if first_row[0] == player_number and second_row[1] == player_number and third_row[2] == player_number:
        if player_number == "1":
            is_player_one_win = True
        else:
            is_player_two_win = True
    elif first_row[2] == player_number and second_row[1] == player_number and third_row[0] == player_number:
        if player_number == "1":
            is_player_one_win = True
        else:
            is_player_two_win = True
    if player_number == "1" and is_player_one_win:
        player_name = "First"
    elif player_number == "2" and is_player_two_win:
        player_name = "Second"
    player_number = int(player_number) + 1

if is_player_one_win or is_player_two_win:
    print(f"{player_name} player won")
else:
    print("Draw!")
