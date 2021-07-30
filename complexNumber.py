class complex:
    def __init__(self, real, img):
        self.real = real
        self.img = img

    def print(self):
        print(self.real, "+", "i" + str(self.img))

    def add(self, obj2):
        self.real += obj2.real
        self.img += obj2.img


c1 = complex(4, 5)
c2 = complex(6, 7)
c1.print()
c2.print()
c1.add(c2)
c1.print()
c2.print()