# Nhập gói tkinter
import tkinter as tk

# Tạo một cửa sổ mới
window = tk.Tk()

# Đặt tiêu đề cho cửa sổ
window.title("python nang cao")

# Tạo một nhãn mới với kiểu phông chữ cụ thể
label = tk.Label(window, text="DHKL16A2", font=("Arial", 20, "bold"))

# Thêm nhãn vào cửa sổ
label.pack()

# Chạy vòng lặp chính của cửa sổ
window.mainloop()
