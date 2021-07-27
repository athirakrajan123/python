class Vehicle:
    def value(self,id_no,model,fuel,price,color):
        self.id_no=id_no
        self.model=model
        self.fuel=fuel
        self.price=price
        self.color=color
    def view(self):
        print("num::",self.id_no,"  model::",self.model,"  fuel::",self.fuel
              ,"  price",self.price,"  color::",self.color)
    def __str__(self):
        return self.model#+"   "+ self.color
       # return self.color only return one return


v1=Vehicle()
v1.value(1001,"nexa","petrol",200000,"gray")
v1.view()
v2=Vehicle()
v2.value(2001,"i10","petrol",100000,"white")
v2.view()
print(v1)#reference of obj v1