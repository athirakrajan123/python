class Stud:
    college="kktm"
    def setval(self,name,roll,mark,course):
        self.name=name
        self.roll=roll
        self.mark=mark
        self.course=course
        #instance variable
    def printval(self):
        print("name::",self.name)
        print("roll::",self.roll)
        print("mark::", self.mark)
        print("course::",self.course)
        print("college::",self.college)
obj =Stud()
name=input("name::")
roll=input("roll::")
mar=input("mark::")
cour=input("course::")
obj.setval(name,roll,mar,cour)
obj.printval()
obj.setval("Athira",24,90,"mca")
obj.printval()