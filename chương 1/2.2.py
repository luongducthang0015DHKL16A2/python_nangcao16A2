danh_sach = []
class TS:
      danh_sach = []
      def __init__(self):
            pass
      def nhap(self):
            so_luong = int(input('Nhập số lượng học sinh: '))
            for i in range(so_luong):
                  ten = input(f'\nNhập tên học sinh thứ {i+1}: ')
                  while True:
                        try:
                              diem_T = float(input(f'Nhập điểm Toán của học sinh thứ {i+1}: '))
                              diem_L = float(input(f'Nhập điểm Lý của học sinh thứ {i+1}: '))
                              diem_H = float(input(f'Nhập điểm Hóa của học sinh thứ {i+1}: '))
                              break
                        except ValueError:
                              print("Điểm phải là một số. Vui lòng nhập lại.")
                  hoc_sinh = {
                  'tên': ten,
                  'điểm toán': diem_T,
                  'điểm lý': diem_L,
                  'điểm hóa': diem_H
                  }
                  danh_sach.append(hoc_sinh)

      def tong_diem(self, hoc_sinh):
            return hoc_sinh['điểm toán'] + hoc_sinh['điểm lý'] + hoc_sinh['điểm hóa']

      def in_ds(self):
            print('Danh sách lớp:')
            for i, hoc_sinh in enumerate(danh_sach, start=1):
                  print(f"\nHọc sinh thứ {i}:")
                  print(f"Tên: {hoc_sinh['tên']}")
                  print(f"Điểm Toán: {hoc_sinh['điểm toán']}")
                  print(f"Điểm Lý: {hoc_sinh['điểm lý']}")
                  print(f"Điểm Hóa: {hoc_sinh['điểm hóa']}")
                  print(f"Tổng điểm: {self.tong_diem(hoc_sinh)}")

      def in_ds_trung_tuyen(self):
            danh_sach_trung_tuyen = [hs for hs in danh_sach if self.tong_diem(hs) >= 20]
            if danh_sach_trung_tuyen:
                  print('\nDanh sách trúng tuyển:')
                  for i, hoc_sinh in enumerate(sorted(danh_sach_trung_tuyen, key=self.tong_diem, reverse=True), start=1):
                        print(f"Học sinh thứ {i}:")
                        print(f"Tên: {hoc_sinh['tên']}")
                        print(f"Điểm Toán: {hoc_sinh['điểm toán']}")
                        print(f"Điểm Lý: {hoc_sinh['điểm lý']}")
                        print(f"Điểm Hóa: {hoc_sinh['điểm hóa']}")
                        print(f"Tổng điểm: {self.tong_diem(hoc_sinh)}")
            else:
                  print("Không có học sinh nào trúng tuyển.")

ds_hs = TS()
ds_hs.nhap()
ds_hs.in_ds()
ds_hs.in_ds_trung_tuyen()
