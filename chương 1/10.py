import math

class da_giac():
      def __init__(self,c_rong):
            self.c_rong=c_rong
            
      def chu_vi(self):
            return sum(self.c_rong)
      
class hinh_binh_hanh(da_giac):
      def __init__(self,c_rong,c_cao,c_dai):
            super().__init__([c_rong, c_dai, c_rong, c_dai])
            self.c_cao=c_cao
                 
      def dien_tich(self):
            return self.c_rong * self.c_cao
      
class hinh_chu_nhat(hinh_binh_hanh):
      def __init__(self,c_dai,c_rong):
            super().__init__(c_dai,c_rong)
            
      def dien_tich(self):
            return self.c_rong * self.c_rong
      
class hinh_vuong(hinh_chu_nhat):
      def __init__(self,c_rong):
            super().__init__(c_rong,c_rong)
            
      def dien_tich(self):
            return self.c_rong * self.c_rong
      
#tạo hình vuông với cạnh cơ sở = 4
tu_giac_deu=hinh_vuong(4)
print('chu vi hình vuông:',tu_giac_deu.chu_vi())
print('dien tich hình vuông:',tu_giac_deu.dien_tich())
print()
#tạo hình hành với cạnh đáy =4 và cao=5
hbh=hinh_binh_hanh(4,7)
print("chu vi hình bình hành là:",hbh.chu_vi())
print("dien tich hinh binh hanh: ",hbh.dien_tich())
hcn=hinh_chu_nhat(4,6)
print("chu vi hình chữ nhật là:",hcn.chu_vi())
print("dien tich hinh chữ nhật là: ",hcn.dien_tich())
