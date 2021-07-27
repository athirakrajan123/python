import re
count=0
matcher=re.finditer('aa','aathiraasaanju')
for match in matcher:
    print("matching index posiition is:",match.start())
    print("matching group is:",match.group())
    count+=1
print("count of matching",count)
#PATTERN MATCHING ONLY IN STRING