from abc import ABC, abstractmethod

class Automobile(ABC):
    def __init__(self, noOfWheels) -> None:
        self.noOfWheels = noOfWheels
        print("Automobile created")

    @abstractmethod
    def start(self):
        print("Start of Automobile called")
    
    @abstractmethod
    def stop(self):
        pass

    @abstractmethod
    def drive(self):
        pass

    @abstractmethod
    def getNoOfWheels(self):
        return self.noOfWheels

class Car(Automobile):
    # def __init__(self, name) -> None:
    #     print("Car Created")
    #     self.name = name
    
    def start(self):
        super().start()
        print("Start of Car Called")

    def stop(self):
        pass

    def drive(self):
        pass

    def getNoOfWheels(self):
        return super().getNoOfWheels()

class Bus(Automobile):
    # def __init__(self, name) -> None:
    #     print("Bus created")    
    #     self.name = name

    def start(self):
        pass

    def stop(self):
        pass

    def drive(self):
        pass

    def getNoOfWheels(self):
        return super().getNoOfWheels()



c = Car(4)
b = Bus(8)
# c.start()
print(c.getNoOfWheels())
print(b.getNoOfWheels())