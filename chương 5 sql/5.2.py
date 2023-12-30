''''viết chương trình python để tạo kết nối cở sở dữ liệu 
SQLite tới cơ sở dữ liệu nằm trong bộ nhớ'''
import sqlite3
conn=sqlite3.connect(':memory:')
conn.close()