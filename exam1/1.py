class Vehicle:
    def detail(self,vnum,year,type):
        self.vnum=vnum
        self.type=type
        self.year=year
class Bus(Vehicle):
    def setdetail(self,name,fuel,color,cost):
        self.name=name
        self.fuel=fuel
        self.color=color
        self.cost=cost
    def display(self):
        print("number",self.vnum)
        print("type",self.type)
        print("year",self.year)
        print("name",self.name)
        print("fuel",self.fuel)
        print("color",self.color)
        print("cost",self.cost)

obj =Bus()
obj.detail("KL45DF678",2010,"bus")
obj.setdetail("motors","petrol","blue",400000)
obj.display()
