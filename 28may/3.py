n = int(input("Enter the rows"))
for i in range(n,0,-1):
    for j in range(i):
        print("* ",end=" ")
    print()