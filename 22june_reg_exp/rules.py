import re
x='[abc]'
count=0
matcher=re.finditer(x,'athirabsanjuc')
print("matching index posiition:::::conatins")
for match in matcher:
    print("    ",match.start(),"     ",match.group())
    count += 1
print("count of matching", count)



import re
x='[^abc]'
count=0
matcher=re.finditer(x,'athirabsanjuc')
for match in matcher:
    print("matching index posiition is:",match.start(),"  conatins :",match.group())
    count += 1
print("count of matching", count)


import re
x='[a-z]'
count=0
matcher=re.finditer(x,'athirabsanjuc68#@AD')
for match in matcher:
    print("matching index posiition is:",match.start(),"  conatins :",match.group())
    count += 1
print("count of matching", count)

import re
x='[A-Z]'
count=0
matcher=re.finditer(x,'athirabsanjuc68#@AD')
for match in matcher:
    print("matching index posiition is:",match.start(),"  conatins :",match.group())
    count += 1
print("count of matching", count)

import re
x='[a-z A-Z]'
count=0
matcher=re.finditer(x,'athirabsanjuc68#@AD')
for match in matcher:
    print("matching index posiition is:",match.start(),"  conatins :",match.group())
    count += 1
print("count of matching", count)

import re
x='[0-9]'
count=0
matcher=re.finditer(x,'athira45657bsanjuc768')
print("matching index::::conatins")
print("posiition")
for match in matcher:
    print("    ",match.start(),"          ",match.group())
    count += 1
print("count of matching", count)



import re
x='[^a-zA-z0-9]'
count=0
matcher=re.finditer(x,'athira4565%$7bsanjuc768')
print("matching index::::conatins")
print("posiition")
for match in matcher:
    print("    ",match.start(),"          ",match.group())
    count += 1
print("count of matching", count)

import re
x='[\s]'
count=0
matcher=re.finditer(x,'athira sanju 768')
print("matching index::::conatins")
print("posiition")
for match in matcher:
    print("    ",match.start(),"          ",match.group())
    count += 1
print("count of matching", count)

import re
x='[\d]'
count=0
matcher=re.finditer(x,'athira sanju 768')
print("matching index::::conatins")
print("posiition")
for match in matcher:
    print("    ",match.start(),"          ",match.group())
    count += 1
print("count of matching", count)

import re
x='[^\d]'
count=0
matcher=re.finditer(x,'athira sanju 768')
print("matching index::::conatins")
print("posiition")
for match in matcher:
    print("    ",match.start(),"          ",match.group())
    count += 1
print("count of matching", count)


import re
x='[\D \w]'
count=0
matcher=re.finditer(x,'athira sanju 768')
print("matching index::::conatins")
print("posiition")
for match in matcher:
    print("    ",match.start(),"          ",match.group())
    count += 1
print("count of matching", count)


import re
x='[\W]'
count=0
matcher=re.finditer(x,'athira@2sanju%%768')
print("matching index::::conatins")
print("posiition")
for match in matcher:
    print("    ",match.start(),"          ",match.group())
    count += 1
print("count of matching", count)