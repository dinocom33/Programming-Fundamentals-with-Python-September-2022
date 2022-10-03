cards = input().split()

team_a = 11
team_b = 11
last_kickoff_player_a = ""
last_kickoff_player_b = ""
game_terminated = False

for card in cards:
    current_card = card.split("-")
    if last_kickoff_player_a == card or last_kickoff_player_b == card:
        continue
    if current_card[0] == "A":
        team_a -= 1
        last_kickoff_player_a = card
    elif current_card[0] == "B":
        team_b -= 1
        last_kickoff_player_b = card
    if team_a < 7 or team_b < 7:
        game_terminated = True
        break

print(f"Team A - {team_a}; Team B - {team_b}")
if game_terminated:
    print("Game was terminated")
