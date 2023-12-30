import threading
import requests

# Danh sách các URL cần thực hiện yêu cầu HTTP
urls = ["https://www.facebook.com/", "https://docs.google.com/document/u/0/"]

def send_request(url):
    response = requests.get(url)
    print(f"Trạng thái phản hồi từ {url}: {response.status_code}\n")

# Tạo và khởi động luồng cho mỗi URL
for url in urls:
    thread = threading.Thread(target=send_request, args=(url,))
    thread.start()
