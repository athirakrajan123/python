import re
n="Athira123A"
x='^[A-Z{1}\w+A-Z{1}$]{5,10}'
match = re.fullmatch(x,n)
if match is not None:
    print("valid  ")
else:
    print("invalid")