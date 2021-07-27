text =input("Enter the String: ")
vowels =['a', 'e', 'i', 'o', 'u']
new = ""
for i in range(len(text)):
    if text[i] not in vowels:
        new =new + text[i]
print("after removing Vowels: ")
text = new
print(text)