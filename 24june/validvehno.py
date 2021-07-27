import re
f=open('regno','r')
ff=open('valid','w')
x = '[K][L][0-9]{2}[A-Z]{2}[0-9]{4}'
for line in f:
    data=line.rstrip("\n")
    match = re.fullmatch(x, data)
    if match is not None:
        print("valid::::", data)
        ff.write(data)
        ff.writelines("\r")
    else:
        print("invalid::",data)
