class Person:
    def setval(self,name,age):
        self.name=name
        self.age=age  #instance variable
    def printval(self):
        print("name::",self.name)
        print("age::",self.age)



obj =Person()
obj.setval("sanju",28)
obj.printval()
obj.setval("Athira",24)
obj.printval()