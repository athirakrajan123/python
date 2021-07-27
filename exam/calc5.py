def add():
    n5=int(input("enter num1:"))
    n6=int(input("enter num2:"))
    print(n5+n6)
def div():
        n7 = int(input("enter num1:"))
        n8 = int(input("enter num2:"))
        print(n7 /n8)
def sub():
    n1=int(input("enter num1:"))
    n2=int(input("enter num2:"))
    print(n1-n2)
def mul():
    n3=int(input("enter num1:"))
    n4=int(input("enter num2:"))
    print(n3*n4)

def floo():
    n9 = int(input("enter num1:"))
    n10= int(input("enter num2:"))
    print(n9//n10)

def ex():
    n11 = int(input("enter num1:"))
    n12= int(input("enter num2:"))
    print(n11** n12)
print("add")
print("sub")
print("mul")
print("div")
print("floor")
print("exp")
choice=int(input("enter choice"))
if choice==1:
    add()

elif choice==2:
    sub()

elif choice ==3:
    mul()
elif choice ==4:
    div()
elif choice == 5:
    floo()
elif choice == 6:
    ex()

