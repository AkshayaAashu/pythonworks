
import pymysql
db=pymysql.connect(host='localhost',user='root',password='aashu3152002@123',database='nov_test')
con=db.cursor()
sqlquery="insert into t1 values(%s,%s,%s)"
val=(22,'adhi',40)
con.execute(sqlquery,val)
db.commit()
print('inserted')


import pymysql
id=int(input("enter the id:"))
na=input("enter the name:")
ag=int(input("enter the age:"))
db=pymysql.connect(host='localhost',user='root',password='aashu3152002@123',database='nov_test')
con=db.cursor()
sql="insert into t1 values(%s,%s,%s)"
val=(id,na,ag)
con.execute(sql,val)
db.commit()
print('inserted successful')