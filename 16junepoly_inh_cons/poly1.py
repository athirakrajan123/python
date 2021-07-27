#overloading
class Oper:
    def num(self,n1,n2):
        self.n1=n1
        self.n2=n2
        print(self.n1+self.n2)
class Dis(Oper):
    def num(self,n3):
        self.n3=n3
        print(self.n3)
d=Dis()
#d.num(2,3)
d.num(3)
"**********************************"

class Oper:
    def num(self,n1,n2):
        self.n1=n1
        self.n2=n2
        print(self.n1+self.n2)
    def num(self, n3):
            self.n3 = n3
            print(self.n3)
d=Oper()
#d.num(2,3)
d.num(6)
