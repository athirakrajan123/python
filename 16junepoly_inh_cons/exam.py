#overriding
class Oper:
    def num(self,n1,n2):
        self.n1=n1
        self.n2=n2
        print(self.n1+self.n2)
class Dis(Oper):
    def num(self,n3,n4):
        self.n3 = n3
        self.n4 = n4
        print(self.n3-self.n4)
d=Dis()
d.num(3,7)
d.num(9,4)


