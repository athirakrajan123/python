import re
def fun(n):
    x='^[A-Z]{1}[a-z0-9\W]+'

    match = re.fullmatch(x,n)
    if match is not None:
        print("valid  ")
    else:
        print("invalid")

while True:
    n=input("enter:")
    fun(n)