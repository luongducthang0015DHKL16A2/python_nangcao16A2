import requests

get_link=requests.get('https://jsonplaceholder.typicode.com/posts ')

if get_link.status_code == 200 :
      json_data=get_link.json()
      for post in json_data: 
            print("ID bài đăng:", post['id']) 
            print("Tiêu đề:", post['title']) 
            print("Nội dung:", post['body']) 
            print("==================================") 
else: 
    print("Yêu cầu không thành công. Mã trạng thái:", get_link.status_code)