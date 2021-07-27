import re
f=open('aaaa','r')
ff=open('valid','w')
x = '[L][U][M][0-9]{2}[P][Y][0-9]{3}'
for line in f:
    data=line.rstrip("\n")
    match = re.fullmatch(x, data)
    if match is not None:
        print(data,"::::","valid" )
        ff.write(data)
        ff.writelines("\r")
    else:
        print(data,"::::","invalid" )
