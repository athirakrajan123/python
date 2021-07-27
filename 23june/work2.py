import re
def fun(n):
    #x = '^a[\w\W]*b$'
    x='^a[a-zA-Z0-9\W]*b$'
    match = re.fullmatch(x,n)
    if match is not None:
        print("valid  ")
    else:
        print("invalid")

while True:
    n=input("enter:")
    fun(n)


