import re
x='a+'
count=0
matcher=re.finditer(x,'aathiraa@2sanju%%768')
print("matching index || conatins")
print("posiition      ||")
for match in matcher:
    print("  ",match.start(),"             ",match.group())
    count += 1
print("count of matching", count)


import re
x='a*'
count=0
matcher=re.finditer(x,'aathiraa@2sanju%%768')
print("matching index || conatins")
print("posiition      ||")
for match in matcher:
    print("  ",match.start(),"             ",match.group())
    count += 1
print("count of matching", count)


import re
x='a?'
count=0
matcher=re.finditer(x,'aathiraa@2sanju%%768')
print("matching index || conatins")
print("posiition      ||")
for match in matcher:
    print("  ",match.start(),"             ",match.group())
    count += 1
print("count of matching", count)


import re
x='a{2}'
count=0
matcher=re.finditer(x,'aathiraa@2sanju%%768')
print("matching index || conatins")
print("posiition      ||")
for match in matcher:
    print("  ",match.start(),"             ",match.group())
    count += 1
print("count of matching", count)


import re
x='a{2,3}'
count=0
matcher=re.finditer(x,'aathiraa@2saaaanju%%768')
print("matching index || conatins")
print("posiition      ||")
for match in matcher:
    print("  ",match.start(),"             ",match.group())
    count += 1
print("count of matching", count)



import re
x='^a'
count=0
matcher=re.finditer(x,'aathiraa@2sanju%%768')
print("matching index || conatins")
print("posiition      ||")
for match in matcher:
    print("  ",match.start(),"             ",match.group())
    count += 1
print("count of matching", count)



import re
x='a$'
count=0
matcher=re.finditer(x,'aathiraa@2sanju%%768a')
print("matching index || conatins")
print("posiition      ||")
for match in matcher:
    print("  ",match.start(),"             ",match.group())
    count += 1
print("count of matching", count)


import re
x='a.'
count=0
matcher=re.finditer(x,'athira@2sanju%%768')
print("matching index || conatins")
print("posiition      ||")
for match in matcher:
    print("  ",match.start(),"             ",match.group())
    count += 1
print("count of matching", count)


import re
x='a|'
count=0
matcher=re.finditer(x,'aathiraa@2sanju%%768')
print("matching index || conatins")
print("posiition      ||")
for match in matcher:
    print("  ",match.start(),"             ",match.group())
    count += 1
print("count of matching", count)



import re
x='a.2'
count=0
matcher=re.finditer(x,'aathira@2sanju%%768')
print("matching index || conatins")
print("posiition      ||")
for match in matcher:
    print("  ",match.start(),"             ",match.group())
    count += 1
print("count of matching", count)



import re
x='^a+'
count=0
matcher=re.finditer(x,'aathiraa@2sanju%%768')
print("matching index || conatins")
print("posiition      ||")
for match in matcher:
    print("  ",match.start(),"             ",match.group())
    count += 1
print("count of matching", count)



import re
x='a*'
count=0
matcher=re.finditer(x,'')
print("matching index || conatins")
print("posiition      ||")
for match in matcher:
    print("  ",match.start(),"             ",match.group())
    count += 1
print("count of matching", count)


