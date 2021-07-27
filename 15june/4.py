class Person:
    def detail(self,name,age,adr):
        self.name = name
        self.age = age
        self.adr = adr
        print("name::", self.name)
        print("age::", self.age)
        print("adr::", self.adr)
class Parent(Person):
    def view(self):
        print("derived class from person")
class Child(Person):
    def views(self):
        print("derived class from person")
class Stud(Child):
    college="kktm"
    def setval(self,name,roll,mark,course):
        self.name=name
        self.roll=roll
        self.mark=mark
        self.course=course
        #instance variable
    def printval(self):
        print("name::",self.name)
        print("roll::",self.roll)
        print("mark::", self.mark)
        print("course::",self.course)
        print("college::",self.college)
obj=Parent()
obj.detail("athira",23,"tcr")
obj.view()
obj1=Stud()
obj1.detail("sanju",28,"kochi")
obj1.views()
obj1.setval("aparna",25,100,"mca")
obj1.printval()