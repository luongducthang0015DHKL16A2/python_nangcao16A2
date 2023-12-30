import sqlite3

# Kết nối đến tệp product1.db
conn = sqlite3.connect('product1.db')

# Tạo con trỏ cursor
c = conn.cursor()
#def  them du lieu
def insert_data():
            while True:
                        id = input("Nhập giá trị id: ")
                        cursor = c.execute("SELECT * FROM product WHERE id=?", (id,))
                        if cursor.fetchone() is None:
                            break
                        else:
                            print("Giá trị id đã tồn tại. Vui lòng nhập lại.")
            name=input('nhập tên sản phẩm:')
            price=input('nhập giá:')
            amount=input('nhập số lượng: ')
            c.execute("INSERT INTO product(id,name,price,amount) VALUES(?,?,?,?)", (id,name,price,amount))
            conn.commit()  
            #su dung vong lap
            while True:
                choice=input('bạn có muốn nhập tiếp không (yes or no) ')
                if  choice=="yes":
                            while True:
                                    id = input("Nhập giá trị id: ")
                                    cursor = c.execute("SELECT * FROM product WHERE id=?", (id,))
                                    if cursor.fetchone() is None:
                                        break
                                    else:
                                        print("Giá trị id đã tồn tại. Vui lòng nhập lại.")

                            name=input('nhập tên sản phẩm:')
                            price=input('nhập giá:')
                            amount=input('nhập số lượng: ')
                            c.execute("UPDATE product SET name=?, price=?, amount=? WHERE id=?", (name, price, amount, id))
                elif choice =="no":
                              break
                else:
                              print("lựa chọn không hợp lệ, vui lòng chọn yes /no")
            return id,name,price,amount
               
                                
def display():
# Thực thi truy vấn SELECT để lấy tất cả các hàng trong bảng product
        c.execute("SELECT * FROM product")

        # Lấy tất cả các hàng trong bảng product
        rows = c.fetchall()
        columns=[description[0] for description in c.description]
        print(columns)

        # In tất cả các hàng ra màn hình
        for row in rows:
            print(row)
#truy van du lieu tu cơ sở dữ liệu
def tim_kiem():
              name=input('nhập tên cần tìm: ')
              c.execute("SELECT * FROM product WHERE name=?", (name,))
              rows=c.fetchall()
              for row in rows:
                            print(row)
              
def delete_id():
              id1=input('nhập id bạn muốn xóa: ')
              c.execute("DELETE from product where id=?",(id1))
              conn.commit()
              print('xóa thành công')
              c.execute("SELECT * FROM product")
              rows=c.fetchall()
              for row in rows:
                            print(row)
def update_product():
              gia=input('nhập giá thay đổi: ')
              so_luong=input('nhập số lượng thay đổi:')
              ma_product=input('nhập id sản phẩm cần thay đổi:')
              c.execute("UPDATE product SET price=?,amount=? WHERE id=?",(gia,so_luong,ma_product) )
              conn.commit()
              print('cập nhật thành công.')
              c.execute("SELECT * FROM product")
              rows=c.fetchall()
              for row in rows:
                            print(row)
def main():
              while True:
                            print("1: nhập dữ liệu")
                            print("2: in thông tin")
                            print("3: xóa sản phẩm")
                            print("4: tìm kiếm sản phẩm")
                            print("5: cập nhật giá và số lượng")
                            choice=input("nhập lựa chọn của bạn: ")
                            if choice =='1':
                                          insert_data()
                            elif choice=='2':
                                          display()
                            elif choice=='3':
                                          delete_id()
                            elif choice=='4':
                                          tim_kiem()
                            else:
                                          update_product()
                                          
if __name__=='__main__':
    main()