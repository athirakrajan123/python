s2=[0,1,2,3,4,5,6,7,8,9,5555,677,89,99,80]
odd=[]
even=[]
for i in s2:
    if i%2==0 or i==0:
        even.append(i)
    elif i%2!=0:
        odd.append(i)
print("odd list",odd)
print("even list",even)




s3=[5,7,3,8,4,9,2]
print(s3)
#s3.sort()
#print(s3)
for ii in range(0, len(s3)):
    for j in range(ii+1, len(s3)):
        if(s3[ii] > s3[j]):
            temp = s3[ii]
            s3[ii] = s3[j]
            s3[j] = temp
print("sorted list is:",s3)

new_list=[]
while s3:
    min=s3[0]
    for iii in s3:
        if iii < min:
            min=iii
    new_list.append(min)
    s3.remove(min)
print("******",new_list)

s4=[5,7,3,8,4,9,2]
new_list1=[]
while s4:
    max=s4[0]
    for iiii in s4:
        if iiii >max:
            max=iiii
    new_list1.append(max)
    s4.remove(max)
print("******",new_list1)