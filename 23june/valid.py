import re
x='\w*'
match=re.fullmatch(x,'hello')
if match is not None:
    print("valid  ")
else:
    print("invalid")

import re
x='\w*'
match=re.fullmatch(x,'20hello')
if match is None:
    print("invalid")
else:
    print("valid")

import re

x = '\w*'
match = re.fullmatch(x, '???hello')
if match is not None:
    print("valid  ")
else:
    print("invalid")




import re

x = '\w*'
match = re.fullmatch(x,'')
if match is not None:
    print("valid  ")
else:
    print("invalid")


import re

x = '\w*'
match = re.fullmatch(x, '56kg')
if match is not None:
    print("valid  ")
else:
    print("invalid")

import re

x = '[0-9]\w*'
match = re.fullmatch(x, '56kg')
if match is not None:
    print("valid  ")
else:
    print("invalid")

import re

x = '\d\w*'
match = re.fullmatch(x, '56kg')
if match is not None:
    print("valid  ")
else:
    print("invalid")

import re

#x = '[0-9]{2}[k][g]'
#x=  '[0-9]{2}[a-z]{2}'
#x='\d{2}kg'
x='[0-9].kg'

match = re.fullmatch(x, '56kg')
if match is not None:
    print("valid  ")
else:
    print("invalid")




