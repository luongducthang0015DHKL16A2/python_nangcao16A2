# Nhập gói tkinter
import tkinter as tk

# Tạo một cửa sổ mới
window = tk.Tk()

# Đặt tiêu đề cho cửa sổ
window.title("Tính GCD và LCM")

# Tạo một khung để chứa nhãn hướng dẫn và hộp văn bản
frame = tk.Frame(window)
frame.pack()

# Tạo nhãn hướng dẫn và hộp văn bản để nhập hai số
tk.Label(frame, text="Nhập số thứ nhất:").grid(row=0, column=0)
entry1 = tk.Entry(frame)
entry1.grid(row=0, column=1)

tk.Label(frame, text="Nhập số thứ hai:").grid(row=1, column=0)
entry2 = tk.Entry(frame)
entry2.grid(row=1, column=1)

# Hàm để tính GCD
def calculate_gcd():
    # Lấy hai số từ hộp văn bản
    a = int(entry1.get())
    b = int(entry2.get())
    # Tính GCD
    while b != 0:
        a, b = b, a % b
    # Hiển thị GCD
    result_label.config(text="GCD của " + str(a) + " và " + str(b) + " là: " + str(a))

# Hàm để tính LCM
def calculate_lcm():
    # Lấy hai số từ hộp văn bản
    a = int(entry1.get())
    b = int(entry2.get())
    # Tính GCD
    gcd = a
    temp = b
    while temp != 0:
        gcd, temp = temp, gcd % temp
    # Tính LCM
    lcm = abs(a*b) // gcd if gcd != 0 else 0
    # Hiển thị LCM
    result_label.config(text="LCM của " + str(a) + " và " + str(b) + " là: " + str(lcm))

# Tạo nút để tính GCD
button_gcd = tk.Button(window, text="Tính GCD", command=calculate_gcd)
button_gcd.pack()

# Tạo nút để tính LCM
button_lcm = tk.Button(window, text="Tính LCM", command=calculate_lcm)
button_lcm.pack()

# Tạo nhãn để hiển thị GCD hoặc LCM
result_label = tk.Label(window, text="")
result_label.pack()

# Chạy vòng lặp chính của cửa sổ
window.mainloop()
