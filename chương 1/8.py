class date:
      def __init__(self,ngay=3,thang=4,nam=5):
            self.ngay=ngay
            self.thang=thang
            self.nam=nam

      def display(self):
            print(f'ngay: {self.ngay}')
            print(f'thang: {self.thang}')
            print(f'nam: {self.nam}')
            
class employee():
      def __init__(self,ho_ten,ngay_sinh,ngay_vao_cty):
            self.ho_ten=ho_ten
            self.ngay_sinh=ngay_sinh
            self.ngay_vao_cty=ngay_vao_cty
      
      def display(self):
            print(f'họ và tên: {self.ho_ten} ')
            print('ngày sinh:')
            self.ngay_sinh.display()
            print('ngày vào công ty:')
            self.ngay_vao_cty.display()
            
ngay_sinh=date(4,6,2004)
ngay_vao_cty=date(5,10,2025)
nhan_vien=employee('luong duc thang',ngay_sinh,ngay_vao_cty)
nhan_vien.display()