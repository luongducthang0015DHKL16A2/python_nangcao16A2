import json
#chuoi python
python_string={"name":"thang",
            "age":"25",
            "address":"thai binh"}

json_obj1=json.dumps(python_string)

for key, value in python_string.items():
          print(value)
print(json_obj1)
print(type(json_obj1))