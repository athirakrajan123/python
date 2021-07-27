import re
def fun(n):
    x='[a-zA-Z\W]*'

    match = re.fullmatch(x,n)
    if match is not None:
        if len(n)>=8 and len(n)<=15:
            print("valid  ")
        else:
            print("invalid")
    else:
        print("invalid")

while True:
    n=input("enter:")
    fun(n)



import re
def fun(n):
    x='[a-zA-Z\W]{8,15}'
    # x='[\D]{8,15}'
    match = re.fullmatch(x,n)
    if match is not None:
        print("valid  ")
    else:
        print("invalid")

while True:
    n=input("enter:")
    fun(n)