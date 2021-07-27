def check(fun):
    def wrapper(n1,n2):
        if n1<n2:
            print(n1, n2, "subtraction not performed")
            return fun(n2,n1)

        else:
            return fun(n1,n2)
    return wrapper

@check
def sub(n1,n2):
    print(n1,n2,"subtration performed==",n1-n2)
sub(20,10)
@check
def num_check(n1,n2):
    print(n1,n2,"changed,result",n1-n2)
num_check(10,20)