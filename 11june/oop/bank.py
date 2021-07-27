class Bank:
    def acc_create(self,num,name,addres,amount):
        self.num = num
        self.name=name
        self.addres=addres
        self.amount=amount
    def viewaccount(self):
        print("num::",self.num)
        print("name::",self.name)
        print("address::",self.addres)
        print("amount::",self.amount)
    def deposit(self,deposit):
        self.deposit=deposit
        print("deposit",self.deposit)
        print("total amount in account:")
        self.amount=self.amount+self.deposit
        print(self.amount)
    def withdraw(self,withdraw):
        self.withdraw=withdraw
        print("withdraw",self.withdraw)
        if (self.withdraw<= self.amount):
            print("total balance in account:")
            self.amount=self.amount-self.withdraw
            print(self.amount)
        else:
            print("insufficient")

obj =Bank()
while True:
    print("****************************************")
    print("1.CREATE, 2.VIEW, 3.DEPOSIT, 4.WITHDRAW")
    print("****************************************")
    op=int(input("choose option::"))
    if op==1:
        num=int(input("number::"))
        name=input("name::")
        addres=input("address::")
        amount=int(input("amount::"))
        obj.acc_create(num,name,addres,amount)
    elif op==2:
        obj.viewaccount()
    elif op==3:
        deposit=int(input("enter amount:"))
        obj.deposit(deposit)
    elif op==4:
        withdraw=int(input("enter amount:"))
        obj.withdraw(withdraw)
    else:
        print("invalid choice")
