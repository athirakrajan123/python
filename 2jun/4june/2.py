s4=[5,7,3,8,4,9,2,5,7]
print(s4)
a=[]
b=[]
for r in s4:
    if r not in a:
        a.append(r)
    else:
        print("duplicates:",r)
print(a)
print("\r")

for i in s4:
    b.append(i*5)
print(b)
c=[ii*5 for ii in s4]
print(b)

print("\r")
list20=[i for i in range(20) if i%2==0]
print(list20)


print("\r")
list20=[i for i in range(1000) if i%8==0]
print(list20)
print(len(list20))

list20=[i for i in range(1,100) if i%5==0]
print(list20)
