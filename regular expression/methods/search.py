import re
# str="class will start at 10am"
# s=re.search('\s',str)
# print(s)
# print(s.start())
# #
# s1=re.search('\d',str)
# print(s1)
#
#
# s2= re.search('python',str)
# print(s2)

str="class will start at 10am"
s=re.search('^class.*10am$',str)
if s:
    print("find")
else:
    print("not find")

#
# #split()
# str="class will start at 10am"
# s=re.split(" ",str)
# print(s)
#
# s1=s=re.split("a",str)
# print(s1)
