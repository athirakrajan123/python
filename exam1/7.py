import re
f=open('nums','r')
ff=open('valid','w')
x ='[+][9][1][0-9]{10}' #\d{10}
for line in f:
    data=line.rstrip("\n")
    match = re.fullmatch(x, data)
    if match is not None:
        print("valid::::", data)
        ff.write(data)
        ff.writelines("\r")
    else:
        print("invalid::",data)
