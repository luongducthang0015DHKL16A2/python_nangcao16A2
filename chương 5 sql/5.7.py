'''viết chương trình python để cập nhật tất cả các giá trị của một cột cụ thể trong
bảng SQLite đã cho'''
import sqlite3
conn=sqlite3.connect('bai4.db')

# cập nhật bản ghi  từ bảng data1
conn.execute(" UPDATE data1 SET 'tên' ='luong ngoc cuong' where id='1'")
conn.commit()
print("tổng số dòng được cập nhật :", conn.total_changes)
cursor=conn.execute(" SELECT * FROM data1")
for row in cursor:
          print(row)
          
conn.close()