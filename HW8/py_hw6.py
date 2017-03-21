class Animal:
    def __init__(self, avg_height, avg_weight, threat_lvl, domestic=True):
        self.height = avg_height
        self.weight = avg_weight
        self.threat_lvl = threat_lvl
        self.domestic = domestic

cat = Animal(0.2, 3, "low", True)
dog = Animal(0.5, 20, "medium", True)
tiger = Animal(1, 60, "high", False)
wolf = Animal(0.5, 30, "high", False)
raccoon = Animal(0.3, 5)

cat.voice = "meow"
dog.voice = "woof"
tiger.voice = "roar"
wolf.voice = "woooooooooof"

print(dog.voice)