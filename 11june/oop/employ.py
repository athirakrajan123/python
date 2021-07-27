class Employee:
    def setval(self,name,age,salary,desig,addres):
        self.name=name
        self.age=age
        self.salary=salary
        self.desig=desig
        self.addres=addres #instance variable
    def printval(self):
        print("************************")
        print("name::",self.name)
        print("age::",self.age)
        print("salary::",self.salary)
        print("designation::",self.desig)
        print("address::",self.addres)
        print("************************")


obj =Employee()
obj.setval("sanju",28,100000,"software_testing",'tcr')
obj.printval()
obj.setval("Athira",24,80000,'developer','tcr')
obj.printval()