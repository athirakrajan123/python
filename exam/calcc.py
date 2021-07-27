print("add")
print("sub")
print("mul")
print("div")
print("floor")
print("exp")
choice=int(input("enter choice"))
n1 = int(input("enter num1:"))
n2 = int(input("enter num2:"))
def add():
    print(n1+n2)
def div():
    print(n1 /n2)
def sub():
    print(n1-n2)
def mul():
    print(n1*n2)
def floo():
    print(n1//n2)
def ex():
    print(n1** n2)
if choice==1:
    add()
elif choice==2:
    sub()
elif choice==3:
    mul()
elif choice==4:
    div()
elif choice==5:
    floo()
elif choice==6:
    ex()

