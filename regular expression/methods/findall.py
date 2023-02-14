import re
# str="rose is a beautiful and colorful flower"
# s=re.findall("bea",str)
# print(s)
#
# s1=re.findall("full",str)
# print(s1)
#
# d="cat mat pat rat sat"
# a=re.findall('[scr]a',d)
# print(a)

# d="cat mat pat rat sat"
# a=re.findall('[^scr]a',d)
# print(a)

# d="cat mat pat rat sat 65454667"
# a=re.findall('\d{3}',d)
# print(a)
#
d="cat mat pat rat sat 6545 46 67789"
a=re.findall('\d{2,3}',d)
print(a)
#
# d="cat mat pat rat sat 6545 46 67"
# a=re.findall(r'\b\d{4}\b',d)
# print(a)






