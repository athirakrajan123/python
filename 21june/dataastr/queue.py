que=[]
r=0
size=int(input("enter the size:"))
def insert(s1):
    global r,size
    if r >= size:
        print("Queue Full!")
    else:
        que.insert(r,s1)
        #que.append(s1)
        r += 1
def delet():
    global r
    if r<=0:
        print(que,"Queue Empty!")
    else:
        try:
            print("deleted element is:",que[0])
            que.remove(que[0])
        except Exception as e:
            print(e,que,"empty queue")


def disp():
    if r <= 0:
        print(que,"Queue Empty!")
    else:
        print("Queue is:",que)

while True:
    print("1.insert  2.delete  3.display")
    print("*************************")
    op=int(input("choose option::"))
    if op==1:
        s1= int(input("enter the element:"))
        insert(s1)
    elif op==2:
        delet()
    elif op==3:
        disp()
    else:
        print("invalid choice")
