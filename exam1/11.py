import re
n="Athira"
x='^[A-Z]{1}[a-z]+'
match = re.fullmatch(x,n)
if match is not None:
    print("valid  ")
else:
    print("invalid")




import re
x='[A-Z]{1}[a-z]+'
count=0
matcher=re.finditer(x,'Athira435646Amith65578Ricxhu')
for match in matcher:
    print("finded:",match.start(),match.group())
    count += 1

print("count of matching", count)
