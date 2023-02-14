"""write a program to read a file line by line and store in to a list"""

def file_read(fna):
    with open (fna) as f:
        output_list=f.readlines()
    print(output_list)
file_read('test1')


#copyfile

from shutil import copyfile
copyfile('test1','test2')
