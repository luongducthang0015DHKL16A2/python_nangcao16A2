import math

class PS:
      def __init__(self):
            self.tu_so=0
            self.mau_so=0
            
      def ktra(self):
            return self.mau_so !=0 and math.gcd(int(self.tu_so),int(self.mau_so)) ==1
      
      def nhap(self):
            while True:
                  try:
                        self.tu_so=float(input('nhập tử số:'))
                        self.mau_so=float(input('nhập mẫu số:'))
                        if self.ktra():
                              break
                        else:
                              print('mẫu số khác không, vui lòng nhập lại.')
                              
                  except ValueError:
                        print('vui lòng nhập lại bằng số:')
      
      def in_ps(self):
            if self.ktra():
                  print(f'phân số của bạn là {self.tu_so}/{self.mau_so}')
            else:
                  print('phân số không hợp lệ')

p_so=PS()
p_so.nhap()
p_so.in_ps()
            