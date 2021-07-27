
def fun(limit):
    sum=0
    for num in range(2,limit+1):
        i=2
        for i in range(2,num):
            if num%i==0:
                i=num
                break
        if i is not num:
            sum+=num
    print("Sum of primes 1 to ",limit,":",sum)
fun(50)