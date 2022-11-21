import re

demons = input().split(",")

health_pattern = r"[^\d\+\-*\/\.]"
damage_pattern = r"([\+\-]?[0-9]+\.?[0-9]*)"
operator_pattern = r"[*\/]"

all_demons = {}
demon_total_health = 0
demon_damage = 0

for current_demon in demons:
    demon = current_demon.strip()
    health = sum(ord(h) for h in (re.findall(health_pattern, demon)))
    damage = re.finditer(damage_pattern, demon)
    operator = re.findall(operator_pattern, demon)
    current_damage = 0
    all_demons[demon] = all_demons.get(demon, {})
    all_demons[demon]["health"] = health
    for digit in damage:
        current_damage += float(digit.group())

    for operator in operator:
        if operator == "*":
            current_damage *= 2
        elif operator == "/":
            current_damage /= 2

    all_demons[demon]["damage"] = current_damage


for demon in sorted(all_demons):
    health = all_demons[demon]["health"]
    damage = all_demons[demon]["damage"]
    print(f"{demon} - {health} health, {damage:.2f} damage")
