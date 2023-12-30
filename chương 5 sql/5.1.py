'''viết chương trình python để tạo một cở sở dữ liệu SQLite ,
    kết nối với cở sở dữ liệu và in ra version của cơ sở dữ liệu SQLite'''
import sqlite3
conect=sqlite3.connect('nhan_vien.db')
print(f"Phiên bản của cơ sở dữ liệu SQLite là {sqlite3.sqlite_version}")