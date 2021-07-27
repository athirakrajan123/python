s2=[0,11,2,3,44,5,6,7,8,9,77,89,99,80,80]
n=int(input("Enter the element to check:  "))
for i in s2:
    if i==n:
        print(n,"is present")
        break
else:
    print(n,"is not present")
print(s2)
s2.sort()
print(s2)
s3=[5,7,3,8,4,9,2]
s3[0]=66
print(s3)
print(s3[0],s3[-1],s3[-2],s3[4])
print(len(s3))
print(s3[1:5])
print(s3[:6])
print(s3[2:])
print(s3[-4:-1],s3[1:6:2])

