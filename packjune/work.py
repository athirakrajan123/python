age=int(input("enter age:::"))
if age<18:
    raise Exception("not eligible for vaccine")
else:
    print("you can take vaccine")