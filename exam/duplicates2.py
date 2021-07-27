testlist =[1,0,7,5,9,2,3,5,7,2,0,1,10]
res=[]
[res.append(x) for x in testlist if x not in res ]
print(" after removing duplicates : ",res)
