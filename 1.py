list1= [2, 4,6,8,10,4,8]
print(list1)
print("after removing duplicates:",list(set(list1)))



s="Athira"
s=list(reversed(s))
new_s=(" ".join(s))
print(new_s)



s= " My name is Athira "
w= s.split()
w= list(reversed(w))
new_s=(" ".join(w))
print(new_s)

s =" My name is Athira "
w = s.split()
new_w= [i[::-1] for i in w]
new_s = " ".join(new_w)
print(new_s)

s =" My name is Athira "
w = s.split()
w= list(reversed(w))
new_w= [i[::-1] for i in w]
new_s = " ".join(new_w)
print(new_s)

