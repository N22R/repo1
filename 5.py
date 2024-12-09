class Fish:
    def __init__(self, name, age, species, size, preferred_food, is_aggressive, needed_space):
        self.name = name
        self.age = age
        self.species = species
        self.size = size
        self.preferred_food = preferred_food
        self.is_aggressive = is_aggressive
        self.needed_space = needed_space

    def __repr__(self):
        return (f"Fish(Name: {self.name}, Age: {self.age}, Species: {self.species}, "
                f"Size: {self.size} cm, Preferred Food: {self.preferred_food}, "
                f"Aggressive: {self.is_aggressive}, Needed Space: {self.needed_space} cubic meters)")

class Aquarium:
    def __init__(self, total_volume, allow_aggressive):
        self.total_volume = total_volume
        self.free_space = total_volume
        self.fishes = []
        self.allow_aggressive = allow_aggressive

    def add_fish(self, fish):
        if self.free_space >= fish.needed_space:
            if self.allow_aggressive and fish.is_aggressive:
                self.fishes.append(fish)
                self.free_space -= fish.needed_space
            elif not self.allow_aggressive and not fish.is_aggressive:
                self.fishes.append(fish)
                self.free_space -= fish.needed_space


    def get_largest_fishes(self):
        largest_fishes = sorted(self.fishes, key=lambda f: f.size, reverse=True)[:3]
        for fish in largest_fishes:
            print(fish)

    def __repr__(self):
        return (f"Aquarium(Total Volume: {self.total_volume} cubic meters, "
                f"Free Space: {self.free_space} cubic meters, Fishes: {len(self.fishes)})")

def main():
    fish1 = Fish("Fish1", 2, "Clownfish", 15, "Plankton", False, 0.5)
    fish2 = Fish("Fish2", 3, "Clownfish", 30, "Plankton", False, 1.0)
    fish3 = Fish("Fish3", 5, "Shark", 250, "Fish", True, 10.0)
    fish4 = Fish("Fish4", 4, "Clownfish", 18, "Plankton", False, 0.7)
    fish5 = Fish("Fish5", 6, "Shark", 150, "Fish", True, 8.0)
    fish6 = Fish("Fish6", 3, "Shark", 100, "Fish", True, 7.0)
    fish7 = Fish("Fish7", 5, "Clownfish", 52, "Plankton", False, 1.8)

    aquarium1 = Aquarium(20, allow_aggressive=False)
    aquarium2 = Aquarium(50, allow_aggressive=True)

    fishes = [fish1, fish2, fish3, fish4, fish5, fish6, fish7]

    for fish in fishes:
        aquarium1.add_fish(fish)
        aquarium2.add_fish(fish)

    print(aquarium1)
    print("Three largest fishes in 1 aquarium:")
    aquarium1.get_largest_fishes()

    print(aquarium2)
    print("Three largest fishes in 2 aquarium:")
    aquarium2.get_largest_fishes()

main()
