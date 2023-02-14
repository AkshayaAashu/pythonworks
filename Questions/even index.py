""""""

str1=input("enter the string:")
print("the string is",str1)
l=len(str1)
print("characters at even index number are:")
for i in range(0,l,2):
    print(str1[i])