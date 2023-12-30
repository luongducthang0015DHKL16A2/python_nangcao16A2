import sqlite3
cre=sqlite3.connect('bai5.db')
# tạo đối tượng con trỏ từ đối tượng kết nối
cursor=cre.cursor()
cursor.execute("SELECT * FROM dta2")
#lấy danh sách các bảng
tables=cursor.fetchall()

# in  danh sách các bảng
print("tổng số bản ghi")
for table in tables:
    print(table)
    
cre.close()
