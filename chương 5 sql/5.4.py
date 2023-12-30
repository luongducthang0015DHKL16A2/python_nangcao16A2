'''viết chương trình python để liệt kê các bảng của tệp cơ sở dữ liệu SQLite đã cho
'''
import sqlite3
cre=sqlite3.connect('bai4.db')
# tạo đối tượng con trỏ từ đối tượng kết nối
cursor=cre.cursor()
cursor.execute("SELECT * FROM data1")
#lấy danh sách các bảng
tables=cursor.fetchall()

# in  danh sách các bảng
print("Các bảng trong cơ sở dữ liệu:")
for table in tables:
    print(table)


