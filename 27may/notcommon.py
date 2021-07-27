a="abcdfg"
b="bcd"
print("not common")
for i in a:
    if i not in b:
        #print("not contains",i)
        print(i)
    elif i in b:
        print("common",i)