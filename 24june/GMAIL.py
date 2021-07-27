import re
def fun(n):
    x = '[a-z0-9]+[@][g][m][a][i][l][.][c][o][m]'#gmail
    #x='[a-zA-Z0-9]+[@][a-z]+[.][a-z]+'
    # x='[a-zA-Z0-9]+[@][a-z]+[.][a-z]{2,3}'
    match = re.fullmatch(x, n)
    if match is not None:
        print("valid  ")
    else:
        print("invalid")


while True:
    n = (input("enter:"))
    fun(n)