class TS:
      def __init__(self):
            self.danh_sach=[]
            
      def nhap(self):
            so_luong=int(input('nhập số lượng danh sách bạn muốn:'))
            for i in range(so_luong):
                  ten=input(f"\nnhập TÊN học sinh thứ {i+1}: ")
                  diem_T=float(input(f"nhập Điểm toán của học sinh thứ {i+1}:"))
                  diem_L=float(input(f"nhập Điểm Ly của học sinh thứ {i+1}: "))
                  diem_H=float(input(f"nhập Điểm Hóa của học sinh thứ {i+1}: "))
                  hoc_sinh={
                        'tên':ten,
                        'điểm toán':diem_T,
                        'điểm lý': diem_L,
                        'điểm hóa': diem_H    
                  }
                  self.danh_sach.append(hoc_sinh)
            
      def tong_diem(self, hoc_sinh):
            return hoc_sinh['điểm toán'] + hoc_sinh['điểm lý'] + hoc_sinh['điểm hóa']
      
      def in_ds(self):
            print('danh sách  :')
            for i, hoc_sinh in enumerate(self.danh_sach, start=1):
                  print(f"\nHọc sinh thứ {i}:")
                  print(f"tên: {hoc_sinh['tên']}")
                  print(f"điểm toán: {hoc_sinh['điểm toán']}")
                  print(f"điểm lý: {hoc_sinh['điểm lý']}")
                  print(f"điểm hóa: {hoc_sinh['điểm hóa']}")
                  print(f"Tổng điểm: {self.tong_diem(hoc_sinh)}")
      
      def in_ds_trung_tuyen(self):
            print('\nDanh sách trúng tuyển:')
            danh_sach_trung_tuyen = [hs for hs in self.danh_sach if self.tong_diem(hs) >= 20]
            danh_sach_trung_tuyen.sort(key=self.tong_diem, reverse=True)
            for i, hoc_sinh in enumerate(danh_sach_trung_tuyen, start=1):
                  print(f"Học sinh thứ {i}:")
                  print(f"Tên: {hoc_sinh['tên']}")
                  print(f"Điểm Toán: {hoc_sinh['điểm toán']}")
                  print(f"Điểm Lý: {hoc_sinh['điểm lý']}")
                  print(f"Điểm Hóa: {hoc_sinh['điểm hóa']}")
                  print(f"Tổng điểm: {self.tong_diem(hoc_sinh)}")
                        
ds_hs=TS()
ds_hs.nhap()
ds_hs.in_ds()
ds_hs.in_ds_trung_tuyen()