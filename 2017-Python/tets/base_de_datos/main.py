import pymysql

db = pymysql.connect (host = '127.0.0.1' , user = "root" , password = "alumno" , db = "classicmodels" , autocommit = True)
c= db.cursor()
c.execute("select productName from products;")
for item in c:
    print(item)