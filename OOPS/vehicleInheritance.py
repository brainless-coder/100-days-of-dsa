class Vehicle:
    def __init__(self, color, maxSpeed) -> None:
        self.color = color
        self.__maxSpeed = maxSpeed
    
    def getMaxSpeed(self):
        return self.__maxSpeed

    def setMaxSpeed(self, maxSpeed):
        self.__maxSpeed = maxSpeed

    def print(self):
        print("Color:", self.color)
        print("Max Speed:", self.__maxSpeed)


class Car(Vehicle):
    def __init__(self, color, maxSpeed, numGears, isConvertible) -> None:
        super().__init__(color, maxSpeed)
        self.numGears = numGears
        self.isConvertible = isConvertible

    def print(self):
        super().print()
        print("NumGears:", self.numGears)
        print("IsConvertible:", self.isConvertible)

c1 = Car("Red", 80, 5, False)
c1.print()
# print()
# v = Vehicle("Blue", 55)
# v.print()