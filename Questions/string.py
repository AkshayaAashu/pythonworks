"""find al of the words in a string that are less than 4 letters"""
sentence=input("enter a sentence:")
words=sentence.split()
print(words)
result=[x for x in words if len(x)<4]
print(result)