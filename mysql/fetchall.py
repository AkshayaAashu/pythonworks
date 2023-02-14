import pymysql
# id=int(input("enter the id:"))
db=pymysql.connect(host='localhost', user='root', password='aashu3152002@123', database='nov_test')
con=db.cursor()
sql='select * from t1'
con.execute(sql)
data=con.fetchall()
for i in data:
    id=i[0]
    na=i[1]
    ag=i[2]
    print(f' id={i[0]},Name={na},Age={ag}')