number_of_dragons = int(input())

all_dragons = {}
damage_dragon = "damage"
health_dragon = "health"
armor_dragon = "armor"


def add_dragon(type_of_dragon, name_of_dragon, damage_of_dragon, health_of_dragon, armor_of_dragon):
    all_dragons[type_of_dragon] = all_dragons.get(dragon_type, dict())
    all_dragons[type_of_dragon][name_of_dragon] = all_dragons.get(dragon_name, dict())
    all_dragons[type_of_dragon][name_of_dragon][damage_dragon] = damage_of_dragon
    all_dragons[type_of_dragon][name_of_dragon][health_dragon] = health_of_dragon
    all_dragons[type_of_dragon][name_of_dragon][armor_dragon] = armor_of_dragon


for current_dragon in range(number_of_dragons):
    dragon_type, dragon_name, damage, health, armor = input().split()
    if damage == "null":
        dragon_damage = 45
    else:
        dragon_damage = int(damage)
    if health == "null":
        dragon_health = 250
    else:
        dragon_health = int(health)
    if armor == "null":
        dragon_armor = 10
    else:
        dragon_armor = int(armor)

    add_dragon(dragon_type, dragon_name, dragon_damage, dragon_health, dragon_armor)

for color in all_dragons:
    damage, health, armor = 0, 0, 0
    for name in all_dragons[color]:
        damage += all_dragons[color][name][damage_dragon]
        health += all_dragons[color][name][health_dragon]
        armor += all_dragons[color][name][armor_dragon]
    total_dragons = len(all_dragons[color])
    print(f"{color}::({(damage / total_dragons):.2f}/{(health / total_dragons):.2f}/{(armor / total_dragons):.2f})")
    for name in sorted(all_dragons[color].keys()):
        print(
            f"-{name} -> damage: {all_dragons[color][name][damage_dragon]}, health: {all_dragons[color][name][health_dragon]}, armor: {all_dragons[color][name][armor_dragon]}")
