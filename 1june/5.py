def triangle(n):
    k=5
    for i in range(0,n):
        for r in range(0,k):
            print(end=" ")
        k=k+1
        for j in range(0,5):
            print("* ", end=" ")
        print("\r")
triangle(5)