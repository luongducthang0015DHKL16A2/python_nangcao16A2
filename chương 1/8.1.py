class employee():
      def __init__(self,ho_ten,ngay_sinh,ngay_vao_cty):
            self.ho_ten=ho_ten
            self.ngay_sinh=ngay_sinh
            self.ngay_vao_cty=ngay_vao_cty
      
      def display(self):
            print(f'họ và tên: {self.ho_ten} ')
            print(f'ngày sinh:{self.ngay_sinh}')
            print(f'ngày vào công ty: {self.ngay_vao_cty}')
            
nhan_vien=employee('luong duc thang','24-03-2004','21-06-2025')
nhan_vien.display()