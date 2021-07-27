list=[3,6,8,9,4,7,10,4]
def search():
    high=len(list)-1
    low=0
    flag=0
    print(list)
    list.sort()
    s=int(input("enter number:" ))
    while low<=high and flag==0:
        mid=(low+high)//2
        if s > list[mid]:
            low=mid+1
        elif s<list[mid]:
            high=mid-1
        elif s==list[mid]:
            flag=1
            break
    if flag==1:
        print("posiition is",mid+1)
    else:
        print("not found")
search()