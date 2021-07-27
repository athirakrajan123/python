class Emp:
    cname="tcs"
    def __init__(self,name,roll,expe):
        self.roll=roll
        self.name=name
        self.expe=expe
    def details(self):
        print(Emp.cname,self.roll,self.name,self.expe)
    def __str__(self):
        return "name::"+self.name+"  exp::"+str(self.expe)

ob=Emp("sanju",39,5)
ob.details()
print(ob)
da=Emp("athira",7,1)
da.details()
print(da)