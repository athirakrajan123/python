class Teach:
    college="kktm"
    def __init__(self,name,id,dept,course):
        self.name=name
        self.id=id
        self.dept=dept
        self.course=course
        #instance variable
    def printval(self):
        print("name::",self.name)
        print("roll::",self.id)
        print("mark::", self.dept)
        print("course::",self.course)
        print("college::",Teach.college)

name=input("name::")
id=input("id::")
dept=input("dept::")
cour=input("course::")
obj =Teach(name,id,dept,cour)
obj.printval()
obj2=Teach("Athira",24,90,"mca")
obj2.printval()