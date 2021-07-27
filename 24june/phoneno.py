import re
def fun(n):
    x='[0-9]{10}' #\d{10}
    match = re.fullmatch(x,n)
    if match is not None:
        print("valid  ")
    else:
        print("invalid")

while True:
    n=(input("enter:"))
    fun(n)