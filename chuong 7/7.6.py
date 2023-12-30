# Nhập gói tkinter
import tkinter as tk

# Tạo một cửa sổ mới
window = tk.Tk()

# Đặt tiêu đề cho cửa sổ
window.title("Đảo ngược từ")

# Tạo một khung để chứa nhãn hướng dẫn và hộp văn bản
frame = tk.Frame(window)
frame.pack()

# Tạo nhãn hướng dẫn
tk.Label(frame, text="Nhập :").grid(row=0, column=0)

# Tạo hộp văn bản để nhập từ
entry = tk.Entry(frame)
entry.grid(row=0, column=1)

# Hàm để đảo ngược từ
def reverse_word():
    # Lấy từ từ hộp văn bản
    word = entry.get()
    # Đảo ngược từ mà không sử dụng bất kỳ chức năng định sẵn nào
    reversed_word = ''
    for char in word:
        reversed_word = char + reversed_word
    # Hiển thị từ đã đảo ngược
    result_label.config(text="Từ đảo ngược: " + reversed_word)

# Tạo nút để đảo ngược từ
button = tk.Button(window, text="Đảo ngược từ", command=reverse_word)
button.pack()

# Tạo nhãn để hiển thị từ đã đảo ngược
result_label = tk.Label(window, text="")
result_label.pack()

# Chạy vòng lặp chính của cửa sổ
window.mainloop()
