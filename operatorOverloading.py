import math

class Point:
    def __init__(self, x, y) -> None:
        self.__x = x
        self.__y = y

    def __str__(self) -> str:
        return f"This point is at ({self.__x}, {self.__y})"

    def __add__(self, point_obj):
        return Point(self.__x + point_obj.__x, self.__y + point_obj.__y)

    def __lt__(self, point_obj):
        return math.sqrt(self.__x**2 + self.__y**2) < math.sqrt(point_obj.__x**2 + point_obj.__y**2)

p1 = Point(1, 3)
p2 = Point(3, 5)
p3 = p1 + p2
print(p3)
print(p2 < p1)