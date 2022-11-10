command = input()

dwarfs = {}

while command != "Once upon a time":
    name, hat_color, physics = command.split(" <:> ")
    physics = int(physics)
    if hat_color not in dwarfs:
        dwarfs[hat_color] = {name: physics}
    else:
        if name not in dwarfs[hat_color]:
            dwarfs[hat_color].update({name: physics})
        else:
            if physics > dwarfs[hat_color][name]:
                dwarfs[hat_color][name] = physics
    command = input()

final_dwarf_dict = {}

for color, color_members in dwarfs.items():
    members = len(color_members)
    for dwarf, physics in color_members.items():
        current_dwarf = f"{dwarf}|{color}"
        final_dwarf_dict[current_dwarf] = {"name": dwarf, "physics": physics, "members": members, "color": color}

for dwarf in sorted(final_dwarf_dict, key=lambda x: (final_dwarf_dict[x]["physics"],
                                                     final_dwarf_dict[x]["members"]), reverse=True):
    current_dwarf = final_dwarf_dict[dwarf]
    print(f"({current_dwarf['color']}) {current_dwarf['name']} <-> {current_dwarf['physics']}")
