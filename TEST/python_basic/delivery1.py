dict=[
['王*龙', '北京市海淀区苏州街大恒科技大厦南座4层'],
['庞*飞', '北京市昌平区汇德商厦四楼403'],
['顾*锐', '江苏省扬州市三垛镇工业集中区扬州市立华畜禽有限公司'],
['王*飞', '上海市徐汇区上海市徐汇区H88越虹广场B座5E'],
['华*升', '北京市海淀区杰睿大厦'],
['唐*宁', '新疆乌鲁木齐市新疆省乌鲁木齐头屯河区火车西站6街']
]
el_city=[]
province=[]
city=[]
pro_json=[]
city_json=[]
#首先把dict内地址取出来
for aa in enumerate(dict):
    dic = aa[1]
    address = dic[1]
    if "省" in address:
        province.append(address)
        add = address.split('省',1)
        pro_json.append(add[0])
        continue
    elif "市" in address:
        province.append(address)
        add = address.split('市', 1)
        pro_json.append(add[0])
        continue
    else:
        el_city.append(address)
# print(province)
pro_list=list(set(pro_json))
# print(pro_list)

# for item in pro_list:
#     print(f"{item}")
#     for aa in enumerate(dict):
#         dic=aa[1]
#         if item in dic[1]:
# 			if dic[1].startswith(item):
#                 print(f"{dic[0]}{dic[1]}")
# 			el_city.append(dic[1])
#         continue




#取出列表内所有的省市

#省市pro_list与地址a[1]进行比较
#打印出省份item






