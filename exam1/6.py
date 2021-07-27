f=open('mark','r')
list1=[]
for i in f:
    data=i.rstrip("\n").split(",")
    name=data[0]
    roll=data[1]
    course=data[2]
    mark=data[3]
    list1.append(mark)
    if max(list1)==data[3]:
        print(data)
print(list1)
print(max(list1))



