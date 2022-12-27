class Person:
    _age = 0
    _name = ""
    _bloodGrp = "A"

    def __init__(self, a, n, bg):
        self._age = a
        self._name = n
        self._bloodGrp = bg

    def printData(self):
        print("Person Name : ", self._name)
        print("Person Age : ", self._age)
        print("Person Blood Grp : ",self._bloodGrp)

class Student(Person):
   __marks = 0
   __class = 10
   __school = "XYZ"


   def __init__(self,m,c,s,a,n,bg):
       self._name = n
       self._age = a
       self._bloodGrp = bg
       self.__marks = m
       self.__class = c
       self.__schhol = s


   def displayInfo(self):
       print("Student Name : ", self._name)
       print("Student Age : ", self._age)
       print("Student Blood Grp : ",self._bloodGrp)


       print("Student Marks : ", self.__marks)
       print("Student Class : ", self.__class)
       print("Student School : ", self.__school)


p1 = Person(23, "Alice", "O+")
p1.printData()
print("-------------------------------------")
s1 = Student(94,12,"KHS",18,"John","O+")
s1.displayInfo()
