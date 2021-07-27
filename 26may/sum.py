num1 = int(input("Enter a number: "))
num2 = int(input("Enter a number: "))
sum=0
if num1 > 1 and num2>1:
    for i in range(num1, num2):
        for ii in range(2,i):
            if (i % ii)==0:
             break
        else:
            print(i, "is a prime number")
            sum=sum+i
    print(sum)