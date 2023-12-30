import json

staff_1={"name":"thang", "age":25, "email":"thang_25@gmail.com"}
staff_2={"name":"cuong","age":20, "email":"cuong_20@gmail.com"}

employees=[staff_1,staff_2]

into_json = json.dumps(employees, sort_keys=True, indent=4)

print(into_json)
