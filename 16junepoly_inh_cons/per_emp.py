class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def printval(self):
        print("name::",self.name,"\n","age::",self.age)
class Emp(Person):
    def __init__(self,sal,desig,name,age):
        super().__init__(name,age)
        self.sal=sal
        self.desig=desig
    def printvals(self):
        print("desig::",self.desig,"\n","salary::",self.sal)
ob=Emp(10000,"doctor","ajith",23)
ob.printval()
ob.printvals()
