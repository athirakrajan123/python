num1 =0
num2 =1
num3=0
count=0
limit=int(input("Enter a number:"))
print("fibonacci series:")
while count<limit:
    print(num1)
    num3=num1+num2
    num1=num2
    num2=num3
    count+=1




