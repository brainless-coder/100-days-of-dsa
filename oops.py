from datetime import date, datetime

class Student:
    # Class attribute
    __passingPercentage = 40
    #self waale jo hai wo instance(obj) attribute hote hai

    def __init__(self, name, age, rollNo,):
        self.__name = name
        self.age = age
        self.rollNo = rollNo

    @classmethod
    def fromBirthYear(cls, name, year, rollNo):
        return cls(name, datetime.today().year - year, rollNo)

    def studentDetails(self):
        self.__name = "Prime"
        print("Name = ", self.__name)
        self.percentage = 80
        print("Percentage = ", self.percentage)

    def isPassed(self):
        if self.percentage > Student.passingPercentage:
            print("Student is passed")
        else:
            print("Student failed")

    @staticmethod
    def welcomeToSchool():
        print("Hey, Welcome to School")

s1 = Student("Ahbishek", 18, 7)
s1._Student__name = "Rohan"     # Name mangling, a way to access private attributes
# obj._classname__varibale
print(s1.__dict__)
# s1.__name = "Prime"
# print(s1.__dict__)
# print(s1.__passingPercentage)
# s1.studentDetails()
# Student.studentDetails(s1)
#class_name.function(obj_name)
# s1.isPassed()
Student.welcomeToSchool()
s1.welcomeToSchool()
# s2 = Student("Rohan", 35)
# print(s2.__dict__)
# s2.isPassed()
s1 = Student.fromBirthYear("Parikh", 1999, 35)
# print(s1.__dict__)