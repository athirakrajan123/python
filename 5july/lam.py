add=lambda num1,num2:num1+num2
print(add)
lst=[1,2,3,4,5,6,7,8,9,10]
f=list(filter(lambda n:n%2==0,lst))
print(f)
sq=list(map(lambda n:n**2,lst))
print(sq)







products=[
    {"item_name":"boost","mrp":290,"stock":50},
    {"item_name":"complan","mrp":240,"stock":0},
    {"item_name":"bournvita","mrp":320,"stock":20},
    {"item_name":"horlicks","mrp":280,"stock":13},
    {"item_name":"nutricharge","mrp":275,"stock":0},
]
n=list(map(lambda product:product["item_name"],products))
print(n)
nn=list(filter(lambda product:product['mrp']<250,products))
print(nn)

h=list(filter(lambda product:product["stock"]==0,products))
print(h)

lst=[1,2,3,4,5,6,7,8,9,10]
def val(nu):
    return  nu**2

s=list(map(val,lst))
print(s)


list1=[2,3,4,8,10,7]
new=list(filter(lambda n:n<5,n-1,list1))
print(new)