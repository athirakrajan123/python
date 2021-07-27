list=[1,2,3,4,5]
sum=0
mul=1
print(list)
for i in list:
    sum=sum+i
    mul=mul*i
print("The sum of list is:",sum)
print("The product of list is:",mul)
list1=[[1,2,3,4,5],[6,7,9,10]]
print(list1)
for j in list1:
    for r in j:
        print(r)

lst=[1,2,3]
pp=[4,5,6]
#lst.append(pp)
print(lst)
lst.extend(pp)
print(lst)