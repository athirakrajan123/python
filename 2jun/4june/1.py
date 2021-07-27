s4=[5,7,3,8,4,9,2]
#s4.sort()
print(s4)
print("minimum value   ",min(s4))
print("minimum value   ",max(s4))
new_list1=[]
new_list2=[]
while s4:
    new_list1.append(max(s4))
    s4.remove(max(s4))
print("******",new_list1)
print(new_list1[0],new_list1[-1])
s5=[5,7,3,8,4,9,2]
while s5:
    new_list2.append(min(s5))
    s5.remove(min(s5))
print("******",new_list2)
print(new_list2[0],new_list2[-1])
