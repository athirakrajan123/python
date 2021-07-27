data=input('enter:')
a=("",">","<",":",";")
rem=""
print(".....punctuation removed data....")
for i in data:
    if i not in a:
        rem = rem + i
        print(i)
print(rem)
if rem==data:
    print("no puntuation marks")