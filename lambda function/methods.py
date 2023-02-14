
"""filter"""

l=[3,7,11,12,2]
lst=list(filter(lambda x:x%2==0,l))
print(lst)

"""map"""
l=[10,2,4,6,10]
lst=list(map(lambda x:x*2,l))
print(lst)

"""reduce"""
from functools import reduce
l1=[1,2,3,4,5]
p=reduce(lambda x,y:x*y,l1)
print(p)