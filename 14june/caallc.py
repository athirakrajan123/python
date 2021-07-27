class Calc:
    def __init__(self,n1,n2):
        self.n1=n1
        self.n2=n2
    def add(self):
        print("add",self.n1+self.n2)
    def div(self):
        print("div",self.n1 /self.n2)
    def sub(self):
        print("sub",self.n1-self.n2)
    def mul(self):
        print("mul",self.n1*self.n2)
    def floo(self):
        print("floor",self.n1//self.n2)
    def ex(self):
        print("exp",self.n1** self.n2)
    def calc(self):
        print("add", self.n1 + self.n2)
        print("div", self.n1 / self.n2)
        print("sub", self.n1 - self.n2)
        print("mul", self.n1 * self.n2)
        print("floor", self.n1 // self.n2)
        print("exp", self.n1 ** self.n2)

n1 = int(input("enter num1:"))
n2 = int(input("enter num2:"))
obj=Calc(n1,n2)
obj.add()
obj.sub()
obj.mul()
obj.div()
obj.floo()
obj.ex()
obj.calc()


