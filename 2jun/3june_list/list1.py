list=[1,2,3,4,3,4,"hello",True]
print(list)
print(type(list))
list1=[]
a=list.remove(list[0])
print(a)
print(list)
print(type(list1))
list1.append("welcome")
list1.append(100)
print(list1)

n=int(input("Enter the size of list:  "))
list2=[]
print("Enter",n,"elements")
for i in range(0,n):
    i=input()
    list2.append(i)
print("The list is:",list2)
for j in list:
    print(j)
list.remove(1)
print(list)
list.clear()
print(list)
del list
print(list)