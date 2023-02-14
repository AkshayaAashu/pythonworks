"""ARBITARY ARGUMENT - saved in tuple format"""

# def color(*args):
#     print(args[0])
#
# color('purple','red','blue')

def colors(w,*args):
    print('normal argument ',w)
    for i in args:
        print(i)
colors('red','white','black')

