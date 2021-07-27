f3=open('fstfile','r')
count={}
for j in f3:
    print(j)
    b = j.rstrip('\n').split(" ")
    print(b)
    for bb in b:
        if bb not in count:
            count.update({bb:1})
        else:
            val=int(count[bb])
            val+=1
            count.update({bb:val})
print(count)

