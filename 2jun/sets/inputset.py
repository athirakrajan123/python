n=int(input("Enter the size of set:  "))
set1=set()
print("Enter",n,"elements")
for i in range(0,n):
    i=input()
    set1.add(i)
print("The set is:",set1)