st=[]
top=0
def push(data):
    global top,size
    if top >= size:
        print("Stack Full!")
    else:
        st.append(data)
        top += 1
def pop():
    global top
    if top <= 0:
        print(st,"Stack Empty!")
    else:
        print("popped element is:",st.pop())
        top -= 1
def disp():
    if top <= 0:
        print(st,"Stack Empty!")
    else:
        print("stack is:",st)


size=int(input("enter the size:"))
while True:
    print("1.push  2.pop  3.display")
    print("*************************")
    op=int(input("choose option::"))
    if op==1:
        s1= int(input("enter the element:"))
        push(s1)
    elif op==2:
        pop()
    elif op==3:
        disp()
    else:
        print("invalid choice")
