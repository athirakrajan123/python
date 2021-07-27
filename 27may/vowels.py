data=input('enter:')
count=0
a=("a","e","o","i","u")
print(".....count of vowels....")
for i in data:
    if i in a:
        print(i)
        count+=1
print(count,"times")
if count==0:
    print("no vowels...")