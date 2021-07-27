limit= int(input("limit? "))
n1, n2 = 0, 1
count = 0
if limit == 1:
   print("Fibonacci sequence upto",limit,":")
   print(n1)
else:
   print("Fibonacci sequence:")
   while count < limit:
       print(n1)
       nth = n1 + n2
       # update values
       n1 = n2
       n2 = nth
       count += 1