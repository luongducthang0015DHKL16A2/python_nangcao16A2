# Nhập gói tkinter
import tkinter as tk

# Tạo một cửa sổ mới
window = tk.Tk()

# Đặt tiêu đề cho cửa sổ
window.title("Tìm các ước của một số")

# Tạo một khung để chứa nhãn hướng dẫn và hộp văn bản
frame = tk.Frame(window)
frame.pack()

# Tạo nhãn hướng dẫn
tk.Label(frame, text="Nhập một số:").grid(row=0, column=0)

# Tạo hộp văn bản để nhập số nguyên
entry = tk.Entry(frame)
entry.grid(row=0, column=1)

# Hàm để tìm các ước của một số
def find_divisors():
    # Lấy số nguyên từ hộp văn bản
    n = int(entry.get())
    # Tìm các ước của số đó
    divisors = [i for i in range(1, n + 1) if n % i == 0]
    # Hiển thị các ước
    result_label.config(text="Các ước của " + str(n) + " là: " + ', '.join(map(str, divisors)))

# Tạo nút để tìm các ước
button = tk.Button(window, text="Tìm các ước", command=find_divisors)
button.pack()

# Tạo nhãn để hiển thị các ước
result_label = tk.Label(window, text="")
result_label.pack()

# Chạy vòng lặp chính của cửa sổ
window.mainloop()
