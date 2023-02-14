"""KEYWORD ARGUMENT - saved in dictionary format"""

def student(stud1,stud2,stud3):
    print('First is ',stud2)
    print('Second is ',stud3)
    print('Third is ',stud1)
student(stud2='amal',stud1='anu',stud3='anju')


def students(**kwargs):
    for i,j in kwargs.items():
        print("%s-->%s"%(i,j))
students(str2='ammu',str1='anu',str3='achu')
