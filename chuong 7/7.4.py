# Nhập gói tkinter
import tkinter as tk

# Tạo một cửa sổ mới
window = tk.Tk()

# Đặt tiêu đề cho cửa sổ
window.title("Thông tin sinh viên")

# Tạo hộp văn bản cho tên sinh viên
tk.Label(window, text="Tên sinh viên:").grid(row=0, column=0)
name_entry = tk.Entry(window)
name_entry.grid(row=0, column=1)

# Tạo hộp văn bản cho id sinh viên
tk.Label(window, text="ID sinh viên:").grid(row=1, column=0)
id_entry = tk.Entry(window)
id_entry.grid(row=1, column=1)

# Tạo hộp văn bản cho mật khẩu
tk.Label(window, text="Mật khẩu:").grid(row=2, column=0)
password_entry = tk.Entry(window, show="*")
password_entry.grid(row=2, column=1)

# Tạo nút gửi
submit_button = tk.Button(window, text="Gửi", command=lambda: print("Đã gửi"))
submit_button.grid(row=3, column=0, columnspan=2)

# Chạy vòng lặp chính của cửa sổ
window.mainloop()
