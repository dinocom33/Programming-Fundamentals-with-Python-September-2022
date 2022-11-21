import re

number_of_messages = int(input())
pattern = r"@([A-Z][a-z]+)[a-zA-Z]*[^\@\-!:>]*:([\d]+)[^@\-\!\:\>]*\!([AD])\![^@\-\!\:\>]*\-\>([\d]+)"
attacked_planets = []
destroyed_planets = []

for message in range(number_of_messages):
    command = input()
    decrypted_message = ""
    count = len(re.findall("[starSTAR]", command))
    for character in command:
        decrypted_message += (chr(ord(character) - count))
    result = re.search(pattern, decrypted_message)
    if result:
        planet_name, population, attack_type, soldier_count = result.groups()
        if attack_type == "A":
            attacked_planets.append(planet_name)
        elif attack_type == "D":
            destroyed_planets.append(planet_name)

attacked_planets = sorted(attacked_planets)
destroyed_planets = sorted(destroyed_planets)

if len(attacked_planets) > 0:
    print(f"Attacked planets: {len(attacked_planets)}")
    for planet in attacked_planets:
        print(f"-> {planet}")
else:
    print(f"Attacked planets: 0")

if len(destroyed_planets) > 0:
    print(f"Destroyed planets: {len(destroyed_planets)}")
    for planet in destroyed_planets:
        print(f"-> {planet}")
else:
    print("Destroyed planets: 0")
