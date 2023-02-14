"""delete query"""
import pymysql
id=int(input("enter the id:"))
# Name=input("enter the name:")
# Age=int(input("enter the age:"))
db=pymysql.connect(host='localhost',user='root',password='aashu3152002@123',database='nov_test')
mycursor=db.cursor()
sql="delete from t1 where id='%d'"%(id)
# val=(id,Name,Age)
mycursor.execute(sql)
db.commit()
print('deleted  successfully')