a="apple"
count=""
for i in a:
    if i not in count:
        count+=i
    elif i in count:
        print("repeted",i)

a="apple"
count={}
for i in a:
    if i not in count:
        count.update({i:1})
    else:
        print("repeted",i)
        break

con=0
for i in a:
    con=a.count(i)
    if con>1:
        break
print("recuursive",i)