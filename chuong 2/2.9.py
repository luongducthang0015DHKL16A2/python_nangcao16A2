import json

with open('company.json', 'r', encoding='utf-8') as f:
      read_cty=json.load(f)

#lấy thông tin company      
company_name=read_cty['ten_cty']
address_cty=read_cty['địa chỉ']
tong_nv=len(read_cty['employees'])
#in thông tin
print("tên công ty:",company_name)
print("địa chỉ :",address_cty)
print("tổng nhân viên :",tong_nv)

#thống kê nhân viên
tap_hop = {}
for employee in read_cty['employees']:
    group = employee['group']
    if group not in tap_hop:
        tap_hop[group] = 0
    tap_hop[group] += 1

print('-----Thống kê nhân viên theo đơn vị------')
#(key,value) 
for i, (unit, count) in enumerate(tap_hop.items(), start=1):
    percentage = (count / tong_nv) * 100
    print(f'{i}./Tên đơn vị: {unit}.')
    print(f'- Số nhân viên: {count}.')
    print(f'- Tỷ lệ: {percentage:.2f}%.')

