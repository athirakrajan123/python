data="My nameM is AAA"
print(data)
data2=""
count=1
for i in data:
    if i not in data2:
        data2=data2+i
else:
    print(i)
    count=count+1
    print(count)


print(data2)



