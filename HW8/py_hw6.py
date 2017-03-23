class Animal:
    def __init__(self, avg_height, avg_weight, threat_lvl, domestic=True):
        self.height = avg_height
        self.weight = avg_weight
        self.threat_lvl = threat_lvl
        self.domestic = domestic

class CatFamily(Animal):
    def voice(self):
        return "Meow"


class DogFamily(Animal):
    def voice(self):
        return "Woof"

class Raccoon(Animal):
    pass

cat = CatFamily(0.2, 3, "low", True)
dog = DogFamily(0.5, 20, "medium", True)
raccoon = Raccoon(0.3, 5, "low", False)

def check_voice(ClassObj):
    try:
        print(ClassObj.voice())
    except AttributeError:
        print("This animal has no voice")

check_voice(cat)
check_voice(dog)
check_voice(raccoon)