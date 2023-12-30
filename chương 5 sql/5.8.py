'''viết chương trình python để cập nhật tất cả các giá trị của một cột cụ thể trong
bảng SQLite đã cho'''
import sqlite3
conn=sqlite3.connect('bai4.db')

# xóa bản ghi từ bảng data1
conn.execute(" DELETE from data1 where id='2'")
conn.commit()
print("tổng số dòng được cập nhật :", conn.total_changes)
cursor=conn.execute(" SELECT * FROM data1")
for row in cursor:
          print(row)
          
conn.close()