# Nhập gói tkinter
import tkinter as tk

# Tạo một cửa sổ mới
window = tk.Tk()

# Đặt tiêu đề cho cửa sổ
window.title("Nhập tên và tuổi")

# Tạo một khung để chứa nhãn hướng dẫn và hộp văn bản
frame = tk.Frame(window)
frame.pack()

# Tạo nhãn hướng dẫn và hộp văn bản để nhập tên
tk.Label(frame, text="Nhập tên của bạn:").grid(row=0, column=0)
name_entry = tk.Entry(frame)
name_entry.grid(row=0, column=1)

# Tạo nhãn hướng dẫn và hộp văn bản để nhập tuổi
tk.Label(frame, text="Nhập tuổi của bạn:").grid(row=1, column=0)
age_entry = tk.Entry(frame)
age_entry.grid(row=1, column=1)

# Hàm để kiểm tra tuổi và trả về thông báo phù hợp
def check_age():
    # Lấy tên và tuổi từ hộp văn bản
    name = name_entry.get()
    age = int(age_entry.get())
    # Kiểm tra tuổi và trả về thông báo phù hợp
    if age >= 18:
        message = "Xin chào, " + name + "! Bạn đã trưởng thành!"
    else:
        message = "Xin chào, " + name + "! Bạn còn nhỏ tuổi!"
    # Hiển thị thông báo
    result_label.config(text=message)

# Tạo nút để kiểm tra tuổi
button = tk.Button(window, text="Kiểm tra tuổi", command=check_age)
button.pack()

# Tạo nhãn để hiển thị thông báo
result_label = tk.Label(window, text="")
result_label.pack()

# Chạy vòng lặp chính của cửa sổ
window.mainloop()
