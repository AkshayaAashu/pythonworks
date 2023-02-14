#split()
import re
str="class will start at 10am"
s=re.split(" ",str)
print(s)

s1=s=re.split("a",str)
print(s1)

s1=s=re.split(" ",str,2)
print(s1)