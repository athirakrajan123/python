a=[1,2,3,4,5]
b=int(input("enter index"))
try:
    print(a[b])
except Exception as e:
    print(e)
finally:
    print("complete")