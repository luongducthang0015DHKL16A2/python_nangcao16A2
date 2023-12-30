#viết chương trình python để tạo nhiều luồng(mulyo threads) và in tên của các luồng đó    
import threading

# Hàm mà mỗi luồng sẽ chạy
def print_thread_name():
    print(f"Hello từ {threading.current_thread().name}\n")

# Tạo và khởi động 5 luồng
for i in range(5):
    thread = threading.Thread(target=print_thread_name, name=f"Thread-{i}")
    thread.start()
