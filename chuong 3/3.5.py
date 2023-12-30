import numpy as np

# Đọc dữ liệu từ tập tin và bỏ qua các dòng không hợp lệ
height = []
with open('heights_1.txt', 'r') as f:
    for line in f:
        try:
            height.append(float(line.strip()))
        except ValueError:
            pass

weight = []
with open('weights_1.txt', 'r') as f:
    for line in f:
        try:
            weight.append(float(line.strip()))
        except ValueError:
            pass

# Kiểm tra xem có đủ dữ liệu không
if len(height) == 0 or len(weight) == 0:
    print("Không có dữ liệu trong tập tin.")
else:
    # Tạo numpy array từ list
    arr_height = np.array(height)
    arr_weight = np.array(weight)

    # Chuyển đổi đơn vị
    arr_height_m = arr_height * 0.0254
    arr_weight_kg = arr_weight * 0.453592

    # Tính BMI
    arr_bmi = arr_weight_kg / (arr_height_m ** 2)

    # Truy xuất giá trị cân nặng ở vị trí index = 50, nếu có thể
    if len(arr_weight_kg) > 50:
        weight_at_50 = arr_weight_kg[50]
        print(f"Giá trị cân nặng ở vị trí index = 50: {weight_at_50}")
    else:
        print("Không thể truy cập vào vị trí index = 50 vì mảng không đủ lớn.")

    # Tạo arr_height_m_100, nếu có thể
    if len(arr_height_m) > 110:
        arr_height_m_100 = arr_height_m[100:111]
        print(f"arr_height_m_100: {arr_height_m_100}")
    else:
        print("Không thể tạo mảng từ vị trí index 100 đến 110 vì mảng không đủ lớn.")

    # Tìm các cầu thủ có bmi < 21
    players_with_bmi_less_than_21 = arr_bmi[arr_bmi < 21]
    print(f"Số lượng cầu thủ có bmi < 21: {len(players_with_bmi_less_than_21)}")

    # Tính chiều cao và cân nặng trung bình
    average_height = np.mean(arr_height_m)
    average_weight = np.mean(arr_weight_kg)
    print(f"Chiều cao trung bình: {average_height}, Cân nặng trung bình: {average_weight}")

    # Tìm chiều cao và cân nặng lớn nhất
    max_height = np.max(arr_height_m)
    max_weight = np.max(arr_weight_kg)
    print(f"Chiều cao lớn nhất: {max_height}, Cân nặng lớn nhất: {max_weight}")

    # Tìm chiều cao và cân nặng nhỏ nhất
    min_height = np.min(arr_height_m)
    min_weight = np.min(arr_weight_kg)
    print(f"Chiều cao nhỏ nhất: {min_height}, Cân nặng nhỏ nhất: {min_weight}")