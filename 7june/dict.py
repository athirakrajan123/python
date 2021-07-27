dict={'name':'sanju','age':'28','education':'btech'}
print(dict)
print(type(dict))
print(dict['name'])
print("dict['name']:",dict['name'])
print("dict['age']:",dict['age'])
dict['age']=29
print(dict)
dic={}
print(dic)
print(type(dic))
dict['jod']="engineer"
dict.update({'loc':'kochi'})
print(dict)
del dict['jod']
print(dict)
dict.clear()
print(dict)
del dict
print(dict)
d={0:10,1:20,}
print(d)
d.update({2:30})
print(d)
a="hello world"
b=a.split(" ")
print(b)
bb=a.split(",")
print(bb)
for i in b:
    print(i)

