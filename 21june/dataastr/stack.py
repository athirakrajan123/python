class Stack:
    def __init__(self,size):
        self.stack =[]
        self.size =size
        self.top =0
    def push(self, data):
        if self.top >= self.size:
            print("Stack Full!")
        else:
            self.stack.append(data)
            self.top += 1
    def pop(self):
        if self.top <= 0:
            print(self.stack,"Stack Empty!")
        else:
            print("poped element is:",self.stack.pop())
            self.top -= 1
    def disp(self):
        if self.top <= 0:
            print(self.stack,"Stack Empty!")
        else:
            print("stack is:",self.stack)

size=int(input("enter the size:"))
s = Stack(size)
while True:
    print("1.push  2.pop  3.display")
    print("*************************")
    op=int(input("choose option::"))
    if op==1:
        s1 = int(input("enter the element:"))
        s.push(s1)
    elif op==2:
        s.pop()
    elif op==3:
        s.disp()
    else:
        print("invalid choice")
