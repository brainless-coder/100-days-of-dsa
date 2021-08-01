class Mother:
    def __init__(self) -> None:
        self.name = "Alexa"

    def print(self):
        print("Print of Mother called")

class Father:
    def __init__(self) -> None:
        self.name = "John"
        super().__init__()

    def print(self):
        print("Print of Father called")

class Child(Father, Mother):
    def __init__(self) -> None:
        super().__init__()

    def print(self):
        print("Name of child is: " + self.name)


c = Child()
# c.printChild()
c.print()
print(Child.mro())
