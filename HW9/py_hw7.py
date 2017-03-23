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

# Iterator, generator & list comprehension

class FileIterator(object):
    def __init__(self, filename):
        self.fd = open(filename, 'r')

    def __iter__(self):
        return self

    def __next__(self):
        line = self.fd.readline()
        if line != '':
            self.line = line
            return self.line
        raise StopIteration


class ListIterator(object):
    def __init__(self, items):
        self.items = items
        self.count = 0

    def __iter__(self):
        return self

    def __next__(self):
        try:
            self.item = self.items[self.count]
            self.count += 1
            return self.item
        except IndexError:
            raise StopIteration


list1 = ListIterator(["something", "cool", "is", "right", "here"])
print(list1.__next__())
print(list1.__next__())
print(list1.__next__())
print(list1.__next__())


class DictIterator(object):
    def __init__(self, items):
        self.items = items

        self.keylist = []
        self.vallist = []
        for key, val in items.items():
            self.keylist.append(key)
            self.vallist.append(val)
        self.count = 0

    def __iter__(self):
        return self

    def __next__(self):
        try:
            self.item1 = self.keylist[self.count]
            self.item2 = self.vallist[self.count]
            self.count += 1
            return self.item1, self.item2
        except IndexError:
            raise StopIteration

dict1 = DictIterator({"cruiser": "rupture",
                  "battlecruiser": "hurricane",
                  "battleship": "tempest"})
print(dict1.__next__())
print(dict1.__next__())
print(dict1.__next__())


def numbers(first=0, last=100, step=1):
    number = first
    while number < last:
        if number % 3 == 0:
            yield number
            number += step
        else:
            number += step

item = numbers()
for num in item:
    print(num, end=" ")

a = [i for i in range(100) if i % 3 == 0]
print(a)