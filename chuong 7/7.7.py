# Nhập gói tkinter
import tkinter as tk

# Tạo một cửa sổ mới
window = tk.Tk()

# Đặt tiêu đề cho cửa sổ
window.title("Tính tổng từ 1 đến n")

# Tạo một khung để chứa nhãn hướng dẫn và hộp văn bản
frame = tk.Frame(window)
frame.pack()

# Tạo nhãn hướng dẫn
tk.Label(frame, text="Nhập một số:").pack(side=tk.LEFT)

# Tạo hộp văn bản để nhập số nguyên
entry = tk.Entry(frame)
entry.pack(side=tk.LEFT)

# Hàm để tính tổng từ 1 đến n
def calculate_sum():
    # Lấy số nguyên từ hộp văn bản
    n = int(entry.get())
    # Tính tổng từ 1 đến n
    total = 0
    for i in range(1, n + 1):
        total += i
    # Hiển thị tổng
    result_label.config(text="Tổng từ 1+2+3...+ " + str(n) + " là: " + str(total))

# Tạo nút để tính tổng
button = tk.Button(window, text="Tính tổng", command=calculate_sum)
button.pack()

# Tạo nhãn để hiển thị tổng
result_label = tk.Label(window, text="")
result_label.pack()

# Chạy vòng lặp chính của cửa sổ
window.mainloop()
