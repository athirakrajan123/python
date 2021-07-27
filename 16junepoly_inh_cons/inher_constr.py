class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def printval(self):
        print(self.name,self.age)
class Stud(Person):
    def __init__(self,roll,mark,name,age):
        super().__init__(name,age)
        self.roll=roll
        self.mark=mark
    def printvals(self):
        print(self.mark,self.roll)
ob=Stud(23,100,"ajith",20)
ob.printval()
ob.printvals()
