#Ergänzen Sie das Programm classSample.py um eine Methode, sodass die maximale Geschwindigkeit der Fortbewegung(z.B. maxSpeed) in m/s als Returnwert geliefert wird. Geben Sie sinnvolle Werte an und geben Sie diese Werte in der Konsole aus.
#Erstellen zu dem Programm classSample.py ein Klassendiagramm, dass die Vererbung darstellt.

#Schreiben Sie das Programm so, dass folgendes Codefragment ausgeführt werden kann:
#z = Zoo()
#z.addAnimal(Hund())
#z.addAnimal(Schlange())
#z.addAnimal(Loewe())
#z.showAnimals()

from abc import ABC, abstractmethod


class Zoo:
    def __init__(self):
        self.animals = []

    def addAnimal(self, animal):
        self.animals.append(animal)

    def showAnimals(self):
        print("The following animals are in the zoo:")
        for animal in self.animals:
            print(animal.name)

    def movement(self):
        for animal in self.animals:
            animal.movement()


class creature(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def getName(self):
        pass

    @abstractmethod
    def setName(self, name):
        pass


class Animal(creature):
    def __init__(self, name, max_speed, movement_type):
        super().__init__(name)
        self.speed = max_speed
        self._movement_type = movement_type

    def getName(self):
        return self.name

    def setName(self, name):
        self.name = name

    @property
    def speed(self):
        return self._speed

    @speed.setter
    def speed(self, max_speed):
        if max_speed < 0:
            raise ValueError("Speed cannot be negative")
        self._speed = max_speed

    def getMaxSpeed(self):
        return self.speed

    def movement(self):
        print(f"A {self.name} is {self._movement_type} with a speed of {self.speed} m/s")


class Snake(Animal):
    pass


class Doggo(Animal):
    pass


class Lion(Animal):
    pass


z = Zoo()
z.addAnimal(Snake("Viper", 15, "crawling"))
z.addAnimal(Doggo("Bulldog", 20, "running"))
z.addAnimal(Lion("Congo", 25, "running"))

z.showAnimals()
z.movement()

