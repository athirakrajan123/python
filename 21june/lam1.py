print(2**3)
a=lambda num:num**3
print(a(7))
print(a(23))
add=lambda num1,num2:num1+num2
print(add(20,40))

word="hello"
print(len(word))
s1=lambda word:word[0]
print(s1(word))
word1="good"
s2=lambda word1:word1[0]
print(s2(word1))


l=[2,3,4,5,6]
l.pop()
print(l)


def size(self):
    return self.top