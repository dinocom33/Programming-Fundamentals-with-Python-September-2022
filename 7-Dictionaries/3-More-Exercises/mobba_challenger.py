command = input()

players_skills = {}

while " -> " in command:
    player, position, skill = command.split(" -> ")
    skill = int(skill)
    if player not in players_skills:
        players_skills[player] = {position: skill}
    else:
        if position not in players_skills[player]:
            players_skills[player].update({position: skill})
        else:
            if skill > players_skills[player][position]:
                players_skills[player][position] = skill
    command = input()

while command != "Season end":
    first_player, second_player = command.split(" vs ")
    if first_player in players_skills and second_player in players_skills:
        for values in players_skills[first_player]:
            if values in players_skills[second_player]:
                if sum(players_skills[first_player].values()) > sum(players_skills[second_player].values()):
                    del players_skills[second_player]
                    break
                elif sum(players_skills[first_player].values()) < sum(players_skills[second_player].values()):
                    del players_skills[first_player]
                    break
    command = input()

total_players_skill = {}
for player in players_skills:
    total_players_skill[player] = sum(players_skills[player].values())

for player, skill in sorted(total_players_skill.items(), key=lambda x: (-x[1], x[0])):
    print(f"{player}: {skill} skill")
    for key, values in sorted(players_skills[player].items(), key=lambda x: (-x[1], x[0])):
        print(f"- {key} <::> {values}")
