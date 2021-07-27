def check(fun):
    def wrapper(name,age):
        print("wrapper")
        if age<18:
            print(name,age,"not eligible")
        else:
            return fun(name,age)
    return wrapper

@check
def vaccine(name,age):
    print(name,age,"eligible")
vaccine("athira",24)
@check
def eligible_check(name,age):
    print(name,age)
eligible_check("appu",16)