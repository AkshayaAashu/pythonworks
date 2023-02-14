
# str='cat mat rat pat cat rat cat mat sat'
# print(str)
# lst=str.split(" ")
# print(lst)
# d={}
# for i in lst:
#     if i in d:
#         d[i]=d[i]+1
#     else:
#         d[i]=1
# print(d)

#using file
f=open('test2','r')
dict={}
for i in f:
    var=i.split(' ')
    for j in var:
        if j not in dict:
            dict[j]=1
    else:
        dict[j]+=1
print(dict)

