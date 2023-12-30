class stack:
      
      def __init__(self,data=None):
            if data is None:
                  data=[]
            self.data= data
                  
      def push(self,*args):
            for args in args:
                  self.data.append(args)
            print(f'ban da them {len(self.data)} phan tu vao danh sach')
            
      def is_Empty(self):
            if len(self.data)==0:
                  print('danh sách trống.')
                  return True
            else:
                  print('danh sách không rỗng.')
                  return False
                  
      def pop(self):
            #nếu ngăn xếp không trống
            if not self.is_Empty():
                  value= self.data.pop() #xóa phần tử cuối cùng
                  print(f'bạn đã xóa phần tử {value} khỏi danh sách.')
                  return value
            else:
                  print('danh sách trống,không thể xóa')
                  return None                     
      #bài 5             
      def count(self):
            print(f'co {len(self.data)} phan tu trong danh sach')
            return len(self.data)
      #bài 6      
      def print(self):
            print('danh sach cua ban la: ',self.data)
            
drawer=stack([])
drawer.push(1)
drawer.pop()
drawer.is_Empty()
drawer.count()
drawer.print()


  
            
            