a="abc"
b="bcd"
for i in a:
    if i in b:
        print("contains",i)
    elif i not in b:
        print("not contains",i)
