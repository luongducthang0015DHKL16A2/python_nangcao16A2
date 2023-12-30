'''viết chương trình tạo một cơ sở dữ liệu SQLite và tạo một bảng nằm trong cơ sở dữ liệu'''
import sqlite3
cre=sqlite3.connect('bai3.db')
curson=cre.cursor()
curson.execute('''
               CREATE TABLE account
               ("name" TEXT,
               "AGES" INTEGER)
               ''')
curson.execute('''
               INSERT INTO account("name","AGES")
               VALUES ('luong duc thang',20)
               ''')
#LUU CAC THAY DOI 
cre.commit()

#truy xuat du lieu tu bang users
curson.execute("SELECT * FROM account")
rows=curson.fetchall()

#in ketes qua 
for row in rows:
          print(row)
          
#dong con tro curson
curson.close()
cre.close()


