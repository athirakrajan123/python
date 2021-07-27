import re
def fun(n):
    #x = '[A-Z]+[a-z]+\d$'
    #x='\w+\d{1}$'
    x='[a-zA-z]+\d$'
    match = re.fullmatch(x,n)
    if match is not None:
        print("valid  ")
    else:
        print("invalid")

while True:
    n=input("enter:")
    fun(n)
