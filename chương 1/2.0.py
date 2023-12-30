class TS:
      def __init__(self):
            self.hoten=0
            self.diem_T=0
            self.diem_L=0
            self.diem_H=0
      
      def nhap(self):
            self.hoten=input("nhap ho ten: ")
            self.diem_T=float(input('nhap diem toan cua ban:'))
            self.diem_L=float(input('nhap diem Ly cua ban :'))
            self.diem_H=float(input('nhap diem Hoa cua ban:'))
      
      def tong_diem(self):
            return self.diem_T + self.diem_H + self.diem_L
      
ts=TS()

ts.nhap()
print('tong diem cua 3 mon la:',ts.tong_diem())      
      
      
            
            
            
            
