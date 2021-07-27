def add(*args):
    print(args)
    sum=0
    for  i in args:
        sum+=i
    print(sum)

add(1,2,3,4,5)