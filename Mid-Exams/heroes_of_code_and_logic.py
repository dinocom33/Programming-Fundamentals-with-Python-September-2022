number_of_heroes = int(input())

all_heroes = {}
max_hp = 100
max_mp = 200

for hero in range(number_of_heroes):
    name, hp, mp = input().split()
    hp = int(hp)
    mp = int(mp)
    all_heroes[name] = all_heroes.get(name, [0, 0])
    all_heroes[name][0] += hp
    all_heroes[name][1] += mp

while True:
    command = input()
    if command == "End":
        break
    current_command = command.split(" - ")
    action, hero_name = current_command[0], current_command[1]
    if action == "CastSpell":
        mp_needed, spell_name = int(current_command[2]), current_command[3]
        if all_heroes[hero_name][1] >= mp_needed:
            all_heroes[hero_name][1] -= mp_needed
            print(f"{hero_name} has successfully cast {spell_name} and now has {all_heroes[hero_name][1]} MP!")
        else:
            print(f"{hero_name} does not have enough MP to cast {spell_name}!")
    elif action == "TakeDamage":
        damage, attacker = int(current_command[2]), current_command[3]
        all_heroes[hero_name][0] -= damage
        if all_heroes[hero_name][0] > 0:
            print(f"{hero_name} was hit for {damage} HP by {attacker} and now has {all_heroes[hero_name][0]} HP left!")
        else:
            del all_heroes[hero_name]
            print(f"{hero_name} has been killed by {attacker}!")
    elif action == "Recharge":
        amount_to_charge = int(current_command[2])
        if all_heroes[hero_name][1] + amount_to_charge > max_mp:
            amount_to_charge = max_mp - all_heroes[hero_name][1]
        all_heroes[hero_name][1] += amount_to_charge
        print(f"{hero_name} recharged for {amount_to_charge} MP!")
    elif action == "Heal":
        amount_to_heal = int(current_command[2])
        if all_heroes[hero_name][0] + amount_to_heal > max_hp:
            amount_to_heal = max_hp - all_heroes[hero_name][0]
        all_heroes[hero_name][0] += amount_to_heal
        print(f"{hero_name} healed for {amount_to_heal} HP!")

for name, values in all_heroes.items():
    print(name)
    print(f"  HP: {values[0]}\n  MP: {values[1]}")
