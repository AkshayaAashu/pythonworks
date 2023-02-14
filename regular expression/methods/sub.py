import re
str='rose and jasmine are flower'
s=re.sub(' ','*',str)
print(s)

str='rose and jasmine are flower'
s=re.sub(' ','*',str,3)
print(s)