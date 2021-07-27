s={0,1,2,3,4,5,6,7,8,9}
sq=set()
print(s)
print("square root of")
for i in s:
    print( i, "=", i * i)
    #print("square root of", i, "=", i**2)
    sq.add(i*i)
print(sq)
#s.remove(0)
#s.clear()
#print(s)
#del s


s2={0,1,2,3,4,5,6,7,8,9,5555,677,89,99,80}
odd=set()
even=set()
for i in s2:
    if i%2==0 or i==0:
        even.add(i)
    elif i%2!=0:
        odd.add(i)
print("odd set",odd)
print("even set",even)

s3={6,9,8,10,99,55,00,598}
comm=set()
for j in s2:
    if j in s3:
        comm.add(j)
print(comm)
s3.sorted()
print(s3)

