#USER DEFINED EXCEPTION
n1=int(input(":::"))
n2=int(input(":::"))
if n1==n2:
    raise Exception("equual nums")
else:
    print(n1%n2)