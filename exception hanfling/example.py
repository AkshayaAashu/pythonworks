try:
    a=int(input("enter the number:"))
    b=int(input("enter the number:"))
    c=a/b
    print("output is:",c)
except Exception as ex:
    print(ex)
except ZeroDivisionError as er:
    print(er)
except ValueError as er:
    print(er)
