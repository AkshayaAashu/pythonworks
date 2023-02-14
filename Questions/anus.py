#write a program to print the strings that start with the letter 'c' and end with the letter 'b'

names=['chb','ydb','thd','hgt','cqyb','cdsjb']
new_names=[x for x in names if x.endswith('b') & x.startswith('c')]
print(new_names)