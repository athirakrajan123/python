import re
f = open('nums', 'r')
x='[+][9][1][0-9]{10}' #\d{10}
for line in f:
    data = line.rstrip("\n")
    match = re.fullmatch(x,data)
    if match is not None:
        print("valid  ",data)
    else:
        print("invalid")


