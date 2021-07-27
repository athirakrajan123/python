emp={
    10:{"id":10,"name":"athira","sal":10000},
    20:{"id":20,"name":"sanju","sal":20000},
    30:{"id":30,"name":"ananthu","sal":30000}
}
print(emp)
print(emp[10])
print(emp[10]["name"])
id=int(input("enter id:"))
if id in emp:
    pro=input("enter property:")
    if pro in emp[id]:
        print(emp[id][pro])
    else:
        print("invalid property")
else:
    print("not valid id")
