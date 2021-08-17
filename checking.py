import pymysql

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
cur2.execute("select Pname, COUNT(1) as count FROM orders GROUP BY Pname ORDER BY count DESC ")
row2 = cur2.fetchall()
con2.commit()
con2.close
for ro2 in row2:
    print(ro2[0],ro2[1])
