count={}
data="hello hi hello"
print(data)
words=data.split(" ")
for word in words:
    if word not in count:
        count.update({word:1})
    else:
        val=int(count[word])
        val+=1
        count.update({word:val})
print(count)

d="athira sanju athira"
print(d)
s=d.split(" ")
print(s)
dict={}
for i in s:
    count=s.count(i)
    dict.update({i:count})
    print(i,count)
print(dict)


