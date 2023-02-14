"""update"""

import pymysql
y=input("Do you want to update?")
if y=='yes':
    db=pymysql.connect(host='localhost',user='root',password='aashu3152002@123',database='nov_test')
    id=int(input("enter the id:"))
    nm=input("enter the name:")
    ag=int(input("enter the age:"))
    c=db.cursor()
    sql="update t1 set Name='%s',Age='%d' where id='%d' "%(nm,ag,id)
    c.execute(sql)
    db.commit()
    print("updated")
elif y=='no':
    print("exit")
else:
    print("invalid")