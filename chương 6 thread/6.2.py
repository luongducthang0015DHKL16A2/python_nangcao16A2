#viết chương trình python sử dụng luồng để tải xuống đồng thời nhiều tệp

import threading
import requests

# Danh sách các URL cần tải xuống
urls = ["https://img1.kienthucvui.vn/uploads/2019/10/09/anh-bau-troi-dep-hoang-hon-huyen-bi_042052103.jpg","https://4.bp.blogspot.com/-JnMDJhpAXag/UkQIJkqx_nI/AAAAAAAAAis/MtEWPPHMJIU/s1600/anh-dep-hinh-nen-thien-nhien-12.jpg"]

def download_file(url):
    response = requests.get(url, stream=True)
    filename = url.split("/")[-1]

    with open(filename, 'wb') as f:
        for chunk in response.iter_content(chunk_size=1024):
            if chunk:
                f.write(chunk)

# Tạo và khởi động luồng cho mỗi URL
for url in urls:
    thread = threading.Thread(target=download_file, args=(url,))
    thread.start()
