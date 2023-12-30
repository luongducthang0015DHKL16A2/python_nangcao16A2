# viết chương trình python để tạo hai luồng để tìm và in các số chẵn và số lẻ từ 30 đến 50
import threading

# Hàm để tìm và in số chẵn
def print_even_numbers():
    for i in range(30, 51):
        if i % 2 == 0:
            print(f"Số chẵn: {i}\n")

# Hàm để tìm và in số lẻ
def print_odd_numbers():
    for i in range(30, 51):
        if i % 2 != 0:
            print(f"Số lẻ: {i}\n")

# Tạo và khởi động luồng cho số chẵn
even_thread = threading.Thread(target=print_even_numbers)
even_thread.start()

# Tạo và khởi động luồng cho số lẻ
odd_thread = threading.Thread(target=print_odd_numbers)
odd_thread.start()

# Đợi cả hai luồng hoàn thành
even_thread.join()
odd_thread.join()
