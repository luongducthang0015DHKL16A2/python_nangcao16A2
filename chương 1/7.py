from datetime import datetime, timedelta

class date:
      def __init__(self,ngay=3,thang=4,nam=5):
            self.ngay=ngay
            self.thang=thang
            self.nam=nam
            self.date_string=f'{self.ngay}-{self.thang}-{self.nam}'
      
      def display(self):
            print(f'ngay: {self.ngay}')
            print(f'thang: {self.thang}')
            print(f'nam: {self.nam}')
      
      def next(self):
            #datetime.strptime để phân tích chuỗi thành đối tượng datetime.
            self.date_ob=datetime.strptime(self.date_string,'%d-%m-%Y')
            self.next_day=self.date_ob + timedelta(days=1)
            #date.strftime  được sử dụng để định dạng một đối tượng datetime thành một chuỗi
            print(f'next day: {self.next_day.strftime("%d-%m-%Y")}')
      
all=date(1,1,1990)
all.display()
all.next()      