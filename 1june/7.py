def fact(n):
    if n==1:
        return 1
    else:
        return n*fact(n-1)
num=2
print("fact",num,fact(num))