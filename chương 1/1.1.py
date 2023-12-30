class HCN:
      def __init__(self):
            self.c_dai=0
            self.c_rong=0
      
      def nhap(self):
            self.c_dai=float(input('nhap chieu dai hcn:'))
            self.c_rong=float(input('nhap chieu rong hcn:'))
      
      def cvi(self):
            return (self.c_dai + self.c_rong)*2
      
      def dien_tich(self):
            return self.c_dai * self.c_rong
      
      def printer(self):
            print('chieu dai:',self.c_dai)
            print('chieu rong:',self.c_rong)
            
hcn=HCN()
hcn.nhap()
hcn.printer()

print("chu vi hinh chu nhat la:",hcn.cvi())
print("dien tich hinh chu nhat la:",hcn.dien_tich())
            
            