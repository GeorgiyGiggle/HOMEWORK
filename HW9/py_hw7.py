class Battleship:
    def __init__(self, signature_radius, mass, inertia, targeting_range):
        self.signature = signature_radius
        self.mass = mass
        self.inertia = inertia
        self.targ_range = targeting_range


class Tempest(Battleship):
    __scan_resolution = 100
    __sensor_strength = {"radar": 0,
                         "magnetometric": 0,
                         "gravimetric": 0,
                         "ladar": 20
                        }
    max_locked_targets = 7

    def battleship_info(self):
        print("scan resolution = " + str(self.__scan_resolution))
        for key, val in self.__sensor_strength.items():
            print(key, val)
        print("Maximum locked targets = " + str(self.max_locked_targets))
        print("Ship type is" + self.__type())

    def __type(self):
        return "Combat"


class Hyperion(Battleship):
    __scan_resolution = 110
    __sensor_strength = {"radar": 0,
                         "magnetometric": 23,
                         "gravimetric": 0,
                         "ladar": 0
                        }
    max_locked_targets = 7

    def battleship_info(self):
        print("scan resolution = " + str(self.__scan_resolution))
        for key, val in self.__sensor_strength.items():
            print(key, val)
        print("Maximum locked targets = " + str(self.max_locked_targets))
        print("Ship type is" + self.__type())

    def __type(self):
        return "Combat"


tempest = Tempest(360, 99500000, 0.116, 67.5)
hyperion = Hyperion(485, 100200000, 0.1178, 60)

try:
    print(hyperion.__scan_resolution)
    print("Should be 110")
except AttributeError:
    print("Smthng wrong")
    hyperion.__scan_resolution = 500
    print(hyperion.__scan_resolution)