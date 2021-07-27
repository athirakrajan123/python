class College:
    cname="university"
    def __init__(self,name,roll):
        self.roll=roll
        self.name=name
    def details(self):
        print(College.cname,self.roll,self.name)
    def __str__(self):
        return str(self.roll)+self.name
        #return self.roll+self.name              ERROR
        #return self.cname+self.name            CORRECT

ob=College("sanju",39)
print(ob)
da=College("athira",7)
print(da)
da.details()