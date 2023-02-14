"""read"""
f=open('test1','r')
print(f.read())
#
# #
# """readline"""
#
# f=open('test1','r')
# print(f.readline())
# print(f.readline())
# print(f.readline())


# """using for loop"""
#
# f=open('test1','r')
# for i in f:
#     print(i)
# f.close()
#
#
# """append"""
# #
# f=open('test1','a')
# f.write('python is a oop')
# f=open('test1','r')
# print(f.read())
# # f.close()
#
#
# """write"""

# f=open('test1','w')
# f.write('python is a oop')
# f=open('test1','r')
# print(f.read())
# f.close()

#
# """seek"""
# #
# f=open('test1','r')
# f.seek(8)
# print(f.readline())
# f.close()
#
# """tell"""
#
f=open('test1','r')
f.readline()
pos=f.tell()
f.close()
print("position is:",pos)