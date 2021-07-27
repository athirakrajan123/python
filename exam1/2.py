class Person:
    def detail(self,name,place,age):
        self.name=name
        self.place=place
        self.age=age
        print("name",self.name)
        print("place",self.place)
        print("age",age)
class Parent(Person):
    def view(self,job,address):
        self.job=job
        self.address=address
        print("job",self.job)
        print("address",self.address)
class Father(Parent):
    def views(self,):
        print(self.name," is father of child",)
class Mother(Parent):
    def mview(self,name):
        self.name=name
        print(self.name, " is mother of child")
class Child(Father,Mother):
    def setval(self,name,age,std):
        self.name=name
        self.age=age
        self.std=std
    def printval(self):
        print("name",self.name)
        print("age",self.age)
        print("std",self.std)

obj=Child()
obj.detail("thomas","tcr",50)
obj.view("business","royal buildings")
obj.views()
obj.mview("lilly")
obj.setval("Amith",10,5)
obj.printval()


