from abc import ABC, abstractmethod


class Creature(ABC):

    def __init__(self) -> None:
        self.name = ""
        self.type = ""

    @abstractmethod
    def attack(self):
        pass

    def describe(self):
        print(f"Your creature is called {self.name} "
              f"and has the type {self.type} ")


class Flameling(Creature):

    def __init__(self) -> None:
        self.name = "Flameling"
        self.type = "Fire"
        self.weapon = "Ember"

    def attack(self):
        print(f"{self.name} is a {self.type} type Creature")
    
    def fight(self):
        print(f"{self.name} uses {self.weapon}!")


class Pyrodon(Creature):
    def __init__(self) -> None:
        self.name = "Pyrodon"
        self.type = "Fire/Flying"
        self.weapon = "Flamethrower"

    def attack(self):
        print(f"{self.name} is a {self.type} type Creature")

    def fight(self):
        print(f"{self.name} uses {self.weapon}!")


class Aquabub(Creature):
    def __init__(self) -> None:
        self.name = "Aquabub"
        self.type = "Water"
        self.weapon = "Water Gun"

    def attack(self):
        print(f"{self.name} is a {self.type} type Creature")

    def fight(self):
        print(f"{self.name} uses {self.weapon}!")


class Torragon(Creature):
    def __init__(self) -> None:
        self.name = "Torragon"
        self.type = "Water"
        self.weapon = "Hydro Pump"

    def attack(self):
        print(f"{self.name} is a {self.type} type Creature")

    def fight(self):
        print(f"{self.name} uses {self.weapon}!")
