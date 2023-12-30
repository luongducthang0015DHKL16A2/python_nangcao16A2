import json
#chuoi json
json_string='{"name":"thang","age":"25","address":"thai binh"}'

json_obj1=json.loads(json_string)

print(json_obj1)
print(type(json_obj1))