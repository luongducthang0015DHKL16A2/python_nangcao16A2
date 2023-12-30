class HCN:
      def __init__(self,c_dai,c_rong):
            self.c_dai=c_dai
            self.c_rong=c_rong
                  
      def cvi(self):
            return (self.c_dai + self.c_rong)*2
      
      def dien_tich(self):
            return self.c_dai * self.c_rong
      
      def printter(self):
            print(f"chieu dai hinh chu nhat la: {self.c_dai}")
            print(f"chieu rong hinh chu nhat la: {self.c_rong}")
            print(f"chu vi hinh chu nhat la: {self.cvi()}")
            print(f"dien tich hinh chu nhat la: {self.dien_tich()}")
                  
hcn=HCN(10,2)
hcn.printter()


            
            