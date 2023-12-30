'''viết chương trình python để tạo một bảng và chèn một số bảng ghi vào bảng đó.
và cuối cùng chọn tất cả các hàng từ bảng và hiển thị các bản ghi'''
import sqlite3

cre=sqlite3.connect('bai5.db')
cursor=cre.cursor()

cursor.execute('''
               CREATE TABLE dta2
               ("name" TEXT,
               "class" INTEGER)
               ''')
cursor.execute('''
               INSERT INTO dta2("name","class")
               VALUES("thang",16)
               ''')
ten=input('nhập tên: ')
lop=int(input('lớp học: '))
#them du lieu
cursor.execute('INSERT INTO dta2("name","class") VALUES (?,?)',(ten,lop))
#lưu các thay đổi
cre.commit
rowa=cre.execute("SELECT * FROM dta2")
for row in rowa:
          print(row)

cre.close()