class Animal:
    def __init__(self,type,owner):
        self.type=type
        self.owner=owner
class Dog(Animal):
    def setval(self,color,cost):
        self.color=color
        self.cost=cost
    def printval(self):
        print("type",self.type)
        print("owner",self.owner)
        print("color",self.color)
        print("cost",self.cost)

obj =Dog("dog","akhil")
obj.setval("black",10000)
obj.printval()