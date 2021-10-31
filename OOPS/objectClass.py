class Circle(object):   # same as class Circle:
    # The object parameter is passed bydefault in each class
    def __init__(self, radius) -> None:
        self.radius = radius

    def __str__(self) -> str:
        return "This is a circle Class"
    
c = Circle(5)
print(c)