def check(fun):
    def wrapper(user,pin):
        if user not in "admin":
            #raise Exception(user,"you are not allowed")
            print(user,"you are not allowed")
        else:
            return fun(user,pin)
    return wrapper

@check
def changepin(user,pin):
    newpin=pin
    print(user,newpin,"your pin changed")

@check
def delacc(user,pin):
    print(user,pin,"your acc deleted")

changepin("admin",20007)
changepin("user1",20099)
delacc("admin",20007)
delacc("user1",20099)
