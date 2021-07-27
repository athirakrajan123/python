class Emp:
    dist="thrissur"
    def __init__(self,name,rela):
        self.name=name
        self.rela=rela
    def details(self):
        print(self.name,self.rela,Emp.dist)
    def __str__(self):
        return "object refer  ::"+self.name
f=open('data','r')
a=Emp(f.readline(),"myself")
a.details()
print(a)
b=Emp(f.readline(),"hus")
b.details()
print(b)
c=Emp(f.readline(),"bro")
c.details()
print(c)
d=Emp(f.readline(),"bro")
d.details()
print(d)