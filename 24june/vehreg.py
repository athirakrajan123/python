import re
def fun(n):
    x='[K][L][0-9]{2}[A-Z]{2}[0-9]{4}'
    
    match = re.fullmatch(x,n)
    if match is not None:
        print("valid  ")
    else:
        print("invalid")

while True:
    n=(input("enter:"))
    fun(n)