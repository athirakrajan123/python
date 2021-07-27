s1={4,7,8,9,44,56}
s2={0,1,2,3,4,5,6,7,8,9,}
prime=set()
nonprime=set()
for i in s2:
    if i>1:
        for j in range(2,i):
            if i%j==0:
                nonprime.add(i)
                break
        else:
            prime.add(i)
print("prime set",prime)
print("nonprime set",nonprime)
print(s1.union(s2))
print(s1.intersection(s2))
print(s1.difference(s2))
