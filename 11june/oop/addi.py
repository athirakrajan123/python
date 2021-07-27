class Sum:
    def setval(self,n1,n2):
        self.n1=n1
        self.n2=n2  #instance variable
    def printval(self):
        print("n1::",self.n1)
        print("n2::",self.n2)
        print("sum ::",self.n1+self.n2)


obj =Sum()
obj.setval(100,500)
obj.printval()
obj.setval(500,200)
obj.printval()