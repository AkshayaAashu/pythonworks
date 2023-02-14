#write a program to extract numbers from a string by using list comprehension
stringg="the room number 45 and 67 are vaccant"
new=[x for x in stringg if x.isdigit()]
print(new)