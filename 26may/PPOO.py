st="luminar technology"
letter=input ("enter the letter to be search::")
for i in st:
    if letter == i:
        print (letter,"letter is present")
        break
else:
    print (letter,"letter is not present")