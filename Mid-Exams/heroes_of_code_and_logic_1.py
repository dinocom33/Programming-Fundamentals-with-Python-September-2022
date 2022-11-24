def collect_heroes(number):
    heroes_collection = {}
    for _ in range(number):
        command = input().split()
        name, hp, mp = command[0], int(command[1]), int(command[2])
        heroes_collection[name] = [hp, mp]
    return heroes_collection


def cast_spell(heroes, name, mp, spell):
    if mp <= heroes[name][1]:
        heroes[name][1] -= mp
        print(f"{name} has successfully cast {spell} and now has {heroes[name][1]} MP!")
    else:
        print(f"{name} does not have enough MP to cast {spell}!")
    return heroes


def take_damage(heroes, name, damage, attacker):
    if heroes[name][0] - damage > 0:
        heroes[name][0] -= damage
        print(f"{name} was hit for {damage} HP by {attacker} and now has {heroes[name][0]} HP left!")
    else:
        print(f"{name} has been killed by {attacker}!")
        del heroes[name]
    return heroes


def recharge(heroes, name, amount):
    if heroes[name][1] + amount > 200:
        amount = 200 - heroes[name][1]
        heroes[name][1] = 200
    else:
        heroes[name][1] += amount
    print(f"{name} recharged for {amount} MP!")
    return heroes


def heal(heroes, name, amount):
    if heroes[name][0] + amount > 100:
        amount = 100 - heroes[name][0]
        heroes[name][0] = 100
    else:
        heroes[name][0] += amount
    print(f"{name} healed for {amount} HP!")
    return heroes


def print_func(heroes):
    for hero, values in heroes.items():
        print(hero)
        print(f"  HP: {values[0]}")
        print(f"  MP: {values[1]}")


def main_func(number):
    heroes_collection = collect_heroes(number)
    while True:
        command = input()
        if command == "End":
            print_func(heroes_collection)
            break
        current_command = command.split(" - ")
        action, hero_name = current_command[0], current_command[1]
        if action == "CastSpell":
            mp_needed, spell_name = int(current_command[2]), current_command[3]
            cast_spell(heroes_collection, hero_name, mp_needed, spell_name)
        elif action == "TakeDamage":
            damage, attacker = int(current_command[2]), current_command[3]
            take_damage(heroes_collection, hero_name, damage, attacker)
        elif action == "Recharge":
            recharge_amount = int(current_command[2])
            recharge(heroes_collection, hero_name, recharge_amount)
        elif action == "Heal":
            heal_amount = int(current_command[2])
            heal(heroes_collection, hero_name, heal_amount)


number_of_heroes = int(input())
main_func(number_of_heroes)
