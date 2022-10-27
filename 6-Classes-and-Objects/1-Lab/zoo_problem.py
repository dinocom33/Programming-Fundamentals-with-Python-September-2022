class Zoo:
    __animals = 0

    def __init__(self, name):
        self.name = name
        self.mammals = []
        self.fishes = []
        self.birds = []

    def add_animal(self, species, name):
        if species == "mammal":
            self.mammals.append(name)
        elif species == "fish":
            self.fishes.append(name)
        elif species == "bird":
            self.birds.append(name)
        Zoo.__animals += 1

    def get_info(self, species):
        mammals = self.mammals
        fishes = self.fishes
        birds = self.birds
        if species == "mammal":
            return f"Mammals in {zoo.name}: {', '.join(mammals)}\nTotal animals: {Zoo.__animals}"
        elif species == "fish":
            return f"Fishes in {zoo.name}: {', '.join(fishes)}\nTotal animals: {Zoo.__animals}"
        elif species == "bird":
            return f"Birds in {zoo.name}: {', '.join(birds)}\nTotal animals: {Zoo.__animals}"


zoo_name = input()
number = int(input())

zoo = Zoo(zoo_name)

for animal in range(number):
    current_animal = input().split(" ")
    species = current_animal[0]
    name = current_animal[1]
    zoo.add_animal(species, name)

species = input()
print(zoo.get_info(species))
