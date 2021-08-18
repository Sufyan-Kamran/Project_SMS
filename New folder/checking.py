import pymysql
from collections import Counter

con = pymysql.connect(host="localhost", user="root", password="", database="employee" )
cur = con.cursor()
cur.execute("select * from orders")
row = cur.fetchall()
con.commit()
con.close
c= []
sum = 0
qty =0
for ro in row:
    sum = sum + ro[6]
    qty = qty + ro[5]
print("Total Sale is " , sum)
print("Total Sales Units is " , qty)

con2 = pymysql.connect(host="localhost", user="root", password="", database="employee" )
cur2 = con2.cursor()
#cur2.execute("select Pname and bill, count(Pname and bill) as value_occurrence from orders group by Pname and bill order by value_occurrence desc limit 100;")
cur2.execute("select MAX(QTY) AS maximum FROM orders limit 100")
row3 = cur2.fetchall()
for ro in row3:
    print(ro[0])

cur2.execute("select Pname,QTY, COUNT(*) AS magnitude FROM orders GROUP BY QTY ORDER BY magnitude DESC LIMIT 100")
row5 = cur2.fetchall()
for ro4 in row5:
    print(ro4)
