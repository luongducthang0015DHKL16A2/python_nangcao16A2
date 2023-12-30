# Nhập gói tkinter
import tkinter as tk

# Tạo một cửa sổ mới
window = tk.Tk()

# Đặt tiêu đề cho cửa sổ
window.title("Tiêu đề")

# Tạo một nhãn mới
label = tk.Label(window, text="nhãn")

# Thêm nhãn vào cửa sổ
label.pack()

# Chạy vòng lặp chính của cửa sổ
window.mainloop()
