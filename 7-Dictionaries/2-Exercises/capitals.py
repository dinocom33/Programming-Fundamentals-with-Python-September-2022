countries = input().split(", ")
capitals = input().split(", ")

dictionary = dict(zip(countries, capitals))

# for country, capitals in dictionary.items():
#    print(f"{country} -> {capitals}")

[print(f"{country} -> {capital}") for (country, capital) in dictionary.items()]
