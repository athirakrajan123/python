print("Enter the marks")
m1=int(input())
m2=int(input())
m3=int(input())
m4=int(input())
m5=int(input())
total=m1+m2+m3+m4+m5
aver=total/5
print("Total mark is",total,"Average mark is",aver)
if total>=90:
    print("A")
elif total>=80 and total<90:
    print("B")
elif total>=70 and total<80:
    print("C")
else:
    print("failed")