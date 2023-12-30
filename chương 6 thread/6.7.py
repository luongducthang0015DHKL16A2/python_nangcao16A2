import threading
import time

def print_message(message):
    start_time = time.strftime("%b %d %H:%M:%S %Y", time.gmtime())
    print(f"Starting {message} at {start_time}\n")
    time.sleep(2)  # Giả sử rằng việc xử lý mất 2 giây
    end_time = time.strftime("%b %d %H:%M:%S %Y", time.gmtime())
    print(f"Exiting {message} at {end_time}\n")

# Danh sách các tác vụ
tasks = ["threading", "facebook", "zalo","yahoo"]

# Tạo và khởi động luồng cho mỗi tác vụ
for task in tasks:
    thread = threading.Thread(target=print_message, args=(task,))
    thread.start()
    thread.join()
